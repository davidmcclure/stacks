

import os
import json
import bz2

from stacks import config
from stacks.utils import checksum, scan_paths
from stacks.json_text import JSONText


class JSONCorpus:

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

    def make_text_path(self, corpus, identifier):

        """
        Form the archive path for a text.

        Args:
            corpus (str)
            identifier (str)

        Returns: str
        """

        name = checksum(identifier)

        prefix = name[:3]
        suffix = name[3:]

        # Form the segment path.
        segment = os.path.join(self.path, corpus, prefix)

        # Join on the file name.
        return os.path.join(segment, suffix+'.json.bz2')

    def insert_text(self, text):

        """
        Flush a text to disk.

        Args:
            text (JSONText)
        """

        text.validate()

        # Form the text path.
        path = self.make_text_path(text.corpus, text.identifier)

        # Ensure the directory exists.
        os.makedirs(os.path.dirname(path), exist_ok=True)

        # Write the JSON.
        text.flush_bz2_json(path)

    def get_text(self, corpus, identifier):

        """
        Read JSON from the corpus.

        Args:
            corpus (str)
            identifier (str)

        Returns: dict
        """

        path = self.make_text_path(corpus, identifier)

        return JSONText.from_bz2_json(path)

    def texts(self):

        """
        Scan all JSON files and generate text instances.

        Yields: JSONText
        """

        for path in scan_paths(self.path, '\.json.bz2$'):
            yield JSONText.from_bz2_json(path)
