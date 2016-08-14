

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

        path = os.path.join(config['data']['raw'], 'price-lab')

        return cls(path)

    def __init__(self, path):

        """
        Canonicalize the corpus path.

        Args:
            path (str)
        """

        self.path = os.path.abspath(path)

    def metadata_path(self):

        """
        Get the path to `metadata.csv`.

        Returns: str
        """

        return os.path.join(self.path, 'metadata.csv')

    def texts_path(self):

        """
        Get texts/ path.

        Returns: str
        """

        return os.path.join(self.path, 'texts')

    def metadata(self):

        """
        Generate rows from `NOVELS_METADATA.csv`.

        Yields: dict
        """

        with open(self.metadata_path(), 'r') as fh:
            yield from csv.DictReader(fh)
