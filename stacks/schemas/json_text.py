

import json
import bz2

from schematics.models import Model
from schematics.types import StringType
from schematics.types.compound import ModelType

from .metadata import Metadata


class JSONText(Model):


    metadata = ModelType(Metadata, default=dict, required=True)

    text = StringType(required=True)


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
