

import csv
import os

from stacks.common.singletons import session
from stacks.corpus.models import Corpus as StacksCorpus

from .jobs import ingest


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

    def ingest(self):

        """
        Queue ingest jobs for each text.
        """

        corpus = StacksCorpus.replace(
            slug='dime-westerns',
            name='Dime Westerns Corpus',
        )

        session.commit()

        corpus.queue_ingest(ingest, [

            dict(
                texts_path=self.texts_path(),
                slug=slug,
                metadata=row,
            )

            for slug, row in self.metadata()

        ])
