

import os
import json

from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String,
    UniqueConstraint,
    Text,
    DateTime,
)

from stacks.singletons import session
from stacks.models import Base
from stacks.json_corpus import JSONCorpus


class Text(Base):


    __tablename__ = 'text'

    __table_args__ = (
        UniqueConstraint('corpus', 'identifier'),
        dict(sqlite_autoincrement=True),
    )

    version = Column(String, nullable=False)

    created_at = Column(DateTime, nullable=False)

    corpus = Column(String, nullable=False)

    identifier = Column(String, nullable=False)

    title = Column(String, nullable=False)

    author_full = Column(String)

    author_first = Column(String)

    author_last = Column(String)

    year = Column(Integer)


    @classmethod
    def ingest(cls):

        """
        Ingest extracted JSON files.

        Args:
            ext_path (str)
        """

        corpus = JSONCorpus.from_env()

        for text in corpus.texts():
            cls.create(**text.to_manifest())

        session.commit()
