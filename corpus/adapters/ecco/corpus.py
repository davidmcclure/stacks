

import os
import scandir
import re

from django.conf import settings


class Corpus:

    @classmethod
    def from_env(cls):

        """
        Wrap the ENV-defined root.
        """

        return cls(settings.CORPUS_ECCO)

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

        pattern = re.compile('[0-9]{10}.xml')

        for root, dirs, files in scandir.walk(self.path):
            for name in files:

                # Match .xml files.
                if pattern.match(name):
                    yield os.path.join(root, name)
