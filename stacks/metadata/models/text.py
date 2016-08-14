

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

from stacks import session
from stacks.ext.corpus import Corpus
from stacks.metadata.models import Base


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

        corpus = Corpus.from_env()

        for text in corpus.texts():
            cls.create(**text.to_native('metadata'))

        session.commit()

    def path(self):

        """
        Form the path to original JSON file.

        Returns: str
        """

        # TODO: Decouple this? Singleton?
        corpus = Corpus.from_env()

        return corpus.text_path(self.corpus, self.identifier)
