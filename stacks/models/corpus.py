

from sqlalchemy import Column, String

from .base import BaseModel


class Corpus(BaseModel):

    __tablename__ = 'corpus'

    name = Column(String, nullable=False)

    slug = Column(String, nullable=False)
