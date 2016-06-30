

from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String,
    UniqueConstraint,
    Text,
)

from sqlalchemy.orm import relationship

from .base import Base


class Text(Base):

    __tablename__ = 'text'

    __table_args__ = (
        UniqueConstraint('corpus_id', 'identifier'),
    )

    corpus_id = Column(
        Integer,
        ForeignKey('corpus.id'),
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
