

import os
import scandir
import re

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

        return cls(settings.CORPUS_ECCO1)

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

        return scan_paths(self.path, '[0-9]{10}\.xml$')

    def ingest(self):

        """
        Queue ingest jobs for each text.
        """

        StacksCorpus.objects.queue_ingest(
            slug='ecco',
            name='Eighteenth Century Collections Online',
            args=self.text_paths(),
            job=ingest,
        )
