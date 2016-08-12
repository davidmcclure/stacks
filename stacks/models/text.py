

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

from stacks.models import Base
from stacks.singletons import session
from stacks.utils import scan_paths


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

    author_name_full = Column(String)

    author_name_first = Column(String)

    author_name_last = Column(String)

    year = Column(Integer)
