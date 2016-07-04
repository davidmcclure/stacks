

import os

from django.conf import settings

from corpus.models import Corpus as StacksCorpus
from corpus.utils import scan_paths

from .jobs import ingest


class Corpus:

    @classmethod
    def from_env(cls):

        """
        Wrap the ENV-defined root.
        """

        return cls(settings.CORPUS_GAIL_AMFIC)

    def __init__(self, path):

        """
        Canonicalize the corpus path.

        Args:
            path (str)
        """

        self.path = os.path.abspath(path)

    def text_paths(self):

        """
        Generate paths to the XML sources.

        Yields: str
        """

        return scan_paths(self.path, '\.xml$')

    def ingest(self):

        """
        Queue ingest jobs for each text.
        """

        StacksCorpus.objects.queue_ingest(
            slug='gail-american-fiction',
            name='Gail American Fiction',
            args=self.text_paths(),
            job=ingest,
        )
