

import os

from stacks.corpus.utils import scan_paths
from stacks.corpus.models import Corpus as StacksCorpus

from stacks.corpus.adapters.litlab.jobs import ingest


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
        Generate a path for each text directory.

        Yields: str
        """

        for author_dir in next(os.walk(self.path))[1]:

            # Get the full author path.
            author_path = os.path.join(self.path, author_dir)

            for text_dir in next(os.walk(author_path))[1]:

                # Yield each text path.
                yield os.path.join(author_path, text_dir)

    def ingest(self):

        """
        Queue ingest jobs for each text.
        """

        corpus = StacksCorpus.replace(
            slug='litlab-c20',
            name='Literary Lab 20th Century Corpus',
        )

        corpus.queue_ingest(ingest, self.text_paths())
