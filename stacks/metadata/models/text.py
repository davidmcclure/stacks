

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
from stacks.utils import grouper

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

    id = Column(Integer, primary_key=True)

    path = Column(
        String,
        nullable=False,
        unique=True,
    )

    version = Column(
        String,
        nullable=False,
    )

    created_at = Column(
        DateTime,
        nullable=False,
    )

    corpus = Column(
        String,
        nullable=False,
        index=True,
    )

    identifier = Column(
        String,
        nullable=False,
    )

    title = Column(
        String,
        nullable=False,
    )

    author_full = Column(String)

    author_first = Column(String)

    author_last = Column(String)

    year = Column(
        Integer,
        index=True,
    )

    @classmethod
    def ingest(cls, n=1000):
        """Ingest extracted JSON files.

        Args:
            ext_path (str)
        """
        corpus = ExtCorpus.from_env()

        groups = grouper(corpus.paths(), n)

        for i, group in enumerate(groups):

            mappings = []
            for path in group:

                # Hydrate the JSON file.
                ext_text = ExtText.from_bz2_json(path)

                # Assign shared fields + path.
                mapping = ext_text.to_native('metadata')
                mapping['path'] = path

                mappings.append(mapping)

            # Bulk-insert the page.
            session.bulk_insert_mappings(cls, mappings)

            print((i+1)*n)

        session.commit()
