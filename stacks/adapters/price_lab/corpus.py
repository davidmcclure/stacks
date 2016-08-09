

import csv
import os


class Corpus:

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
