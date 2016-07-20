

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
    def replace(cls, **kwargs):

        """
        Delete an existing corpus with the passed slug, create a new one.

        Returns: Corpus
        """

        slug = kwargs.get('slug')

        # Delete the existing corpus.
        cls.query.filter_by(slug=slug).delete()

        # Create a new corpus.
        return cls.create(**kwargs)

    def queue_ingest(self, job, args):

        """
        Queue text ingest jobs.

        Args:
            job (func)
            args (iter)
        """

        for arg in args:

            if type(arg) == dict:
                rq.enqueue(job, self.id, **arg)

            else:
                rq.enqueue(job, self.id, arg)
