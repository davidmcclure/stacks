

import csv
import os

from stacks import config


class Corpus:

    @classmethod
    def from_env(cls):

        """
        Wrap the ENV-defined directory.

        Returns: cls
        """

        path = os.path.join(config['data']['raw'], 'chicago')

        return cls(path)

    def __init__(self, path):

        """
        Canonicalize the corpus path.

        Args:
            path (str)
        """

        self.path = os.path.abspath(path)

    def novels_metadata_path(self):

        """
        Get the path to `NOVELS_METADATA.csv`.

        Returns: str
        """

        return os.path.join(self.path, 'NOVELS_METADATA.csv')

    def novels_metadata(self):

        """
        Generate rows from `NOVELS_METADATA.csv`.

        Yields: dict
        """

        with open(self.novels_metadata_path(), 'r') as fh:
            yield from csv.DictReader(fh)
