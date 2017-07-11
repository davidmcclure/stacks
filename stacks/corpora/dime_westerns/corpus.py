

import csv
import os

from stacks import config


class Corpus:

    @classmethod
    def from_env(cls):
        """Wrap the ENV-defined directory.

        Returns: cls
        """
        path = os.path.join(config['data']['raw'], 'dime-westerns')

        return cls(path)

    def __init__(self, path):
        """Canonicalize the corpus path.

        Args:
            path (str)
        """
        self.path = os.path.abspath(path)

    def texts_path(self):
        """Get texts/ path.

        Returns: str
        """
        return os.path.join(self.path, 'texts')

    def metadata(self):
        """Generate rows from the CSVs.

        Yields: dict
        """
        for slug in [
            'BBL',
            'BBS',
            'BDN',
            'BNYD',
            'HDL',
            'WWW',
        ]:

            path = os.path.join(self.path, '{0}.csv'.format(slug))

            with open(path, 'r') as fh:
                for row in csv.DictReader(fh):
                    yield (slug, row)
