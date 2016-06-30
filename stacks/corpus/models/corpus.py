

import re

from sqlalchemy import Column, String, UniqueConstraint
from sqlalchemy.orm import validates

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

            assert re.match('^[a-z0-9-]+$', val), (
                'Slugs can only contain letters, numbers, and underscores.'
            )

        return val
