

import os
import scandir

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

        return cls(settings.CORPUS_CHADH_POETRY)

    def __init__(self, path):

        """
        Canonicalize the corpus path.

        Args:
            path (str)
        """

        self.path = os.path.abspath(path)

    def source_paths(self):

        """
        Generate paths to the XML sources.

        Yields: str
        """

        return scan_paths(self.path, '\.new$')

    def ingest(self):

        """
        Queue ingest jobs for each text.
        """

        # TODO: Ingest the segments as separate corpora?

        StacksCorpus.objects.queue_ingest(
            slug='chadwyck-healey-poetry',
            name='Chadwyck Healey Poetry',
            args=self.source_paths(),
            job=ingest,
        )
