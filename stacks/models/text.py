

from sqlalchemy import Column, Integer, ForeignKey, String

from .base import Base


class Text(Base):

    __tablename__ = 'text'

    corpus_id = Column(Integer, ForeignKey('corpus.id'))

    identifier = Column(String, nullable=False)
