

import os
import json

from schema import Schema, Optional

from stacks.common.singletons import config
from stacks.corpus.utils import checksum


class ExtCorpus:

    schema = Schema({

        'identifier': str,
        'title': str,
        'plain_text': str,

        Optional('author_name_full'): str,
        Optional('author_name_first'): str,
        Optional('author_name_last'): str,
        Optional('year'): int,

    })

    @classmethod
    def from_env(cls):

        """
        Wrap the ENV-defined root.

        Returns: cls
        """

        return cls(config['data']['ext'])

    def __init__(self, path):

        """
        Canonicalize the root path.

        Args:
            path (str)
        """

        self.path = os.path.abspath(path)

    def flush(self, corpus, data):

        """
        Write a text to disk.

        Args:
            corpus (str)
            data (dict)
        """

        data = self.schema.validate(data)

        name = checksum(data['identifier'])

        prefix = name[:3]
        suffix = name[3:]

        # Form the segment path.
        segment = os.path.join(self.path, corpus, prefix)

        # Ensure the directory exists.
        os.makedirs(segment, exist_ok=True)

        # Form the text path.
        path = os.path.join(segment, suffix+'.json')

        with open(path, 'w') as fh:
            json.dump(data, fh, indent=2)
