

import json
import bz2

from datetime import datetime as dt

from schematics.types import StringType, IntType, DateTimeType
from schematics.models import Model

from stacks.schema_types import MetadataType
from stacks.singletons import version


class JSONText(Model):


    version = StringType(default=version, required=True)

    created_at = DateTimeType(default=dt.now, required=True)

    corpus = StringType(required=True)

    identifier = StringType(required=True)

    title = StringType(required=True)

    plain_text = StringType(required=True)

    author_name_full = MetadataType()

    author_name_first = MetadataType()

    author_name_last = MetadataType()

    year = IntType()


    @classmethod
    def from_bs2_json(cls, path):

        """
        Inflate a compressed JSON file.

        Args:
            path (str)

        Returns: cls
        """

        with bz2.open(path, 'rt') as fh:
            return cls(json.load(fh))

    def as_manifest(self):

        """
        Map the JSON payload into a database row.

        Returns: dict
        """

        row = self.to_native()

        # Omit plain text.
        row.pop('plain_text')

        return row
