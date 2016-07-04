

import os
import scandir

from django.conf import settings

from corpus.models import Corpus as StacksCorpus

from .jobs import ingest


class Corpus:

    @classmethod
    def from_env(cls):

        """
        Wrap the ENV-defined root.
        """

        return cls(settings.CORPUS_NCCO)

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

        for root, dirs, files in scandir.walk(self.path):
            for name in files:

                # Match .xml files.
                if os.path.splitext(name)[1] == '.xml':
                    yield os.path.join(root, name)

    def ingest(self):

        """
        Queue ingest jobs for each text.
        """

        StacksCorpus.objects.queue_ingest(
            slug='ncco',
            name='Nineteenth Century Collections Online',
            args=self.text_paths(),
            job=ingest,
        )
