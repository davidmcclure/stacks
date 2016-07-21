

import csv
import os

from stacks.corpus.models import Corpus as StacksCorpus
from stacks.common.singletons import session

from .jobs import ingest


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

    def ingest(self):

        """
        Queue ingest jobs for each text.
        """

        args = [
            dict(texts_path=self.texts_path(), metadata=row)
            for row in self.metadata()
        ]

        corpus = StacksCorpus.replace(
            slug='price-lab',
            name='Price Lab Corpus',
        )

        session.commit()

        corpus.queue_ingest(ingest, args)
