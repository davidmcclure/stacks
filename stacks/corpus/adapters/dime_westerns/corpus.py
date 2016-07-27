

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

    def texts_path(self):

        """
        Get texts/ path.

        Returns: str
        """

        return os.path.join(self.path, 'texts')

    def metadata(self):

        """
        Generate rows from the CSVs.

        Yields: dict
        """

        for slug in ['BBL']:

            path = os.path.join(self.path, '{0}.csv'.format(slug))

            with open(path, 'r') as fh:
                yield from csv.DictReader(fh)
