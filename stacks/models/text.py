

from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String,
    UniqueConstraint,
)

from sqlalchemy.orm import relationship

from .base import Base


class Text(Base):

    __tablename__ = 'text'

    __table_args__ = (
        UniqueConstraint('corpus_id', 'identifier'),
    )

    corpus_id = Column(Integer, ForeignKey('corpus.id'), nullable=False)

    corpus = relationship('Corpus')

    identifier = Column(String, nullable=False)
