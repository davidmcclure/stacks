

import re

from sqlalchemy import Column, String, UniqueConstraint
from sqlalchemy.orm import validates

from stacks.common.singletons import session, rq
from stacks.common.models import Base


class Corpus(Base):


    __tablename__ = 'corpus'

    __table_args__ = (
        UniqueConstraint('slug'),
    )

    name = Column(String, nullable=False)

    slug = Column(String, nullable=False)


    @validates('slug')
    def validate_slug(self, key, val):

        """
        Check the slug format.

        Args:
            key (str)
            val (mixed)

        Raises: AssertionError
        """

        if type(val) is str:

            assert re.match('^[a-z0-9-]+$', val), \
                'Slugs can only contain letters, numbers, and underscores.'

        return val


    @classmethod
    def queue_ingest(cls, slug, name, args, job):

        """
        Reset a corpus and queue text ingest jobs in RQ.

        Args:
            slug (str)
            name (str)
            args (iter)
            job (func)
        """

        # Delete the existing corpus.
        session.query(cls).filter_by(slug=slug).delete()

        # Create a new corpus.
        corpus = cls.create(slug=slug, name=name)
        session.flush()

        # Spool a job for each source.
        for arg in args:

            if type(arg) == dict:
                rq.enqueue(job, corpus.id, **arg)

            else:
                rq.enqueue(job, corpus.id, arg)
