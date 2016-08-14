

import os

from stacks import config
from stacks.utils import checksum, scan_paths
from .text import Text


class Corpus:

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

    def text_path(self, corpus, identifier):

        """
        Form the JSON path for a text.

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
        Write a text as compressed JSON into the corpus.

        Args:
            text (Text)
        """

        text.validate()

        # Form the text path.
        path = self.text_path(text.corpus, text.identifier)

        # Ensure the directory exists.
        os.makedirs(os.path.dirname(path), exist_ok=True)

        # Write the JSON.
        text.flush_bz2_json(path)

    def get_text(self, corpus, identifier):

        """
        Hydrate a text instance from the JSON.

        Args:
            corpus (str)
            identifier (str)
        """

        path = self.text_path(corpus, identifier)

        return Text.from_bz2_json(path)

    def paths(self):

        """
        Scan JSON file paths.

        Yields: str
        """

        yield from scan_paths(self.path, '\.json.bz2$')

    def texts(self):

        """
        Scan JSON files and generate text instances.

        Yields: Text
        """

        for path in self.paths():
            yield Text.from_bz2_json(path)
