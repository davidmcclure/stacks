

from sqlalchemy import Column, String

from .base import Base


class Corpus(Base):

    __tablename__ = 'corpus'

    name = Column(String, nullable=False)

    slug = Column(String, nullable=False)
