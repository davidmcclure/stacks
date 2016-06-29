

from sqlalchemy import Column, String, UniqueConstraint

from .base import Base


class Corpus(Base):

    __tablename__ = 'corpus'

    __table_args__ = (
        UniqueConstraint('slug'),
    )

    name = Column(String, nullable=False)

    slug = Column(String, nullable=False)
