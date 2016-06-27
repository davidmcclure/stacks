

import os

from django.conf import settings

from corpus.models import Corpus as StacksCorpus
from corpus.adapters.litlab.jobs import ingest


class Corpus:


    @classmethod
    def from_env(cls):

        """
        Wrap the ENV-defined root.

        Returns: cls
        """

        return cls(settings.CORPUS_LITLAB_C20)


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

        StacksCorpus.objects.queue_ingest(
            slug='litlab-c20',
            name='Literary Lab 20th Century Corpus',
            paths=self.text_paths(),
            job=ingest,
        )
