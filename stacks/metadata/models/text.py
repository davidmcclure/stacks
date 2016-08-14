

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
from stacks.metadata.models import Base

from stacks.ext import (
    Text as ExtText,
    Corpus as ExtCorpus,
)


class Text(Base):

    __tablename__ = 'text'

    __table_args__ = (
        UniqueConstraint('corpus', 'identifier'),
        dict(sqlite_autoincrement=True),
    )

    path = Column(String, nullable=False, unique=True)

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

        corpus = ExtCorpus.from_env()

        for path in corpus.paths():

            ext_text = ExtText.from_bz2_json(path)

            # Mass assign shared fields.
            text = cls.create(**ext_text.to_native('metadata'))

            # Set the absolute file path.
            text.path = path

        session.commit()
