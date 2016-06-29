

from sqlalchemy import Column, Integer, ForeignKey, String

from .base import BaseModel


class Text(BaseModel):

    __tablename__ = 'text'

    corpus_id = Column(Integer, ForeignKey('corpus.id'))

    identifier = Column(String, nullable=False)
