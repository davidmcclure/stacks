

import os
import scandir

from django.conf import settings
from corpus.utils import scan_ext


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

        return scan_ext(self.path, '.new')
