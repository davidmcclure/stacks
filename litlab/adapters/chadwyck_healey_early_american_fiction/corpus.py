

import glob
import os

from litlab.conf import settings

from corpora.models import Text
from corpora.adapters import QueueAdapter


class Corpus(QueueAdapter):


    name = 'Chadwyck Healey Early American Fiction'

    slug = 'chadwyck-healey-early-american-fiction'


    @classmethod
    def from_env(cls):

        """
        Wrap the settings-defined path.
        """

        return cls(settings.LITLAB_CHADWYCK_HEALEY_EARLY_AMERICAN_FICTION)


    @classmethod
    def job(cls, corpus_id, path):

        """
        Ingest volumes from a source path.

        Args:
            corpus_id (int): The id of the parent corpus.
            path (str): The path of the source file.
        """

        pass


    def __init__(self, path):

        """
        Set the corpus path.

        Args:
            path (str): The corpus path.
        """

        self.path = os.path.abspath(path)


    def paths(self):

        """
        Generate text paths.

        Yields:
            str: The next path
        """

        return glob.glob(os.path.join(self.path, '*.new'))
