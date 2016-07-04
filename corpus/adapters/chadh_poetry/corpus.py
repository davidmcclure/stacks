

import os
import scandir

from django.conf import settings


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

    def text_paths(self):

        """
        Generate paths to the XML sources.

        Yields: str
        """

        for root, dirs, files in scandir.walk(self.path):
            for name in files:

                # Match .new files.
                if os.path.splitext(name)[1] == '.new':
                    yield os.path.join(root, name)
