

import os

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

    def text_paths(self):

        """
        Generate paths to the XML sources.

        Yields: str
        """

        return scan_paths(self.path, '\.xml.gz$')

    def ingest(self):

        """
        Queue ingest jobs for each text.
        """

        corpus = StacksCorpus.replace(
            slug='eebo',
            name='Early English Books Online',
        )

        corpus.queue_ingest(ingest, self.text_paths())
