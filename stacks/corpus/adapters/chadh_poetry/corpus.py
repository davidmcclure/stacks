

import os
import scandir

from stacks.corpus.utils import scan_paths
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

        corpus = StacksCorpus.replace(
            slug='chadwyck-healey-poetry',
            name='Chadwyck Healey Poetry',
        )

        corpus.queue_ingest(ingest, self.source_paths())
