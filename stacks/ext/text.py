

import json
import bz2

from datetime import datetime as dt

from schematics.models import Model
from schematics.types import StringType, IntType, DateTimeType
from schematics.transforms import blacklist

from stacks.utils import git_rev
from .schema_types import MetadataType


class Text(Model):

    version = StringType(
        default=git_rev(),
        required=True,
    )

    created_at = DateTimeType(
        default=dt.now,
        required=True,
    )

    corpus = StringType(
        required=True,
    )

    identifier = StringType(
        required=True,
    )

    title = StringType(
        required=True,
    )

    plain_text = StringType(
        required=True,
    )

    author_full = MetadataType()

    author_first = MetadataType()

    author_last = MetadataType()

    year = IntType()

    class Options:
        roles = dict(metadata=blacklist('plain_text'))

    @classmethod
    def from_bz2_json(cls, path):

        """
        Inflate a compressed JSON file.

        Args:
            path (str)

        Returns: cls
        """

        with bz2.open(path, 'rt') as fh:
            return cls(json.load(fh))

    def flush_bz2_json(self, path):

        """
        Write a compressed JSON file.

        Args:
            path (str)
        """

        with bz2.open(path, 'wt') as fh:
            json.dump(self.to_primitive(), fh)
