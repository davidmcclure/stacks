

import hashlib

from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String,
    UniqueConstraint,
    Text,
)

from sqlalchemy.orm import relationship, validates

from stacks.common.models import Base


class Text(Base):


    __tablename__ = 'text'

    __table_args__ = (
        UniqueConstraint('corpus_id', 'identifier'),
    )

    corpus_id = Column(
        Integer,
        ForeignKey('corpus.id', ondelete='CASCADE'),
        nullable=False,
    )

    corpus = relationship('Corpus')

    identifier = Column(String, nullable=False)

    title = Column(String, nullable=False)

    author_name_full = Column(String)

    author_name_first = Column(String)

    author_name_last = Column(String)

    year = Column(Integer)

    plain_text = Column(Text, nullable=False)


    # TODO: test
    @validates(
        'title',
        'author_name_full',
        'author_name_first',
        'author_name_last',
    )
    def strip(self, key, val):

        """
        Strip whitespace.

        Args:
            key (str)
            val (mixed)
        """

        return val.strip() if type(val) is str else val
