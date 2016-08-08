

import os
import json

from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String,
    UniqueConstraint,
    Text,
)

from sqlalchemy.orm import relationship, validates

from stacks.common.models import Base
from stacks.common.singletons import session
from stacks.corpus.utils import scan_paths


class Text(Base):


    __tablename__ = 'text'

    __table_args__ = (
        UniqueConstraint('corpus', 'identifier'),
        dict(sqlite_autoincrement=True),
    )

    corpus = Column(String, nullable=False)

    identifier = Column(String, nullable=False)

    title = Column(String, nullable=False)

    author_name_full = Column(String)

    author_name_first = Column(String)

    author_name_last = Column(String)

    year = Column(Integer)


    @validates(
        'title',
        'author_name_full',
        'author_name_first',
        'author_name_last',
    )
    def strip_whitespace(self, key, val):

        """
        Strip whitespace.

        Args:
            key (str)
            val (mixed)
        """

        return val.strip() if type(val) is str else val

    @classmethod
    def ingest(cls, ext_path, corpus):

        """
        Ingest extracted texts.

        Args:
            ext_path (str)
            corpus (str)
        """

        corpus_dir = os.path.join(ext_path, corpus)

        # Scan JSON files.
        for path in scan_paths(corpus_dir, '\.json'):
            with open(path, 'r') as fh:

                # Read the JSON.
                data = json.load(fh)

                cls.create(

                    corpus=corpus,
                    identifier=data.get('identifier'),
                    title=data.get('title'),

                    author_name_full=data.get('author_name_full'),
                    author_name_first=data.get('author_name_first'),
                    author_name_last=data.get('author_name_last'),
                    year=data.get('year'),

                )

        session.commit()
