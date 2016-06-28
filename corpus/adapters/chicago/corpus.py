

import csv
import os

from django.conf import settings
from corpus.models import Corpus as StacksCorpus

from .jobs import ingest


class Corpus:

    @classmethod
    def from_env(cls):

        """
        Wrap the ENV-defined root.
        """

        return cls(settings.CORPUS_CHICAGO)

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
            for row in csv.DictReader(fh):
                yield row

    def ingest(self):

        """
        Queue ingest jobs for each text.
        """

        args = [
            [self.path, row]
            for row in self.novels_metadata()
        ]

        StacksCorpus.objects.queue_ingest(
            slug='chicago',
            name='Chicago Corpus',
            args=args,
            job=ingest,
        )
