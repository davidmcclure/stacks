

import glob
import os

from litlab.conf import settings

from corpora.models import Text
from corpora.adapters import QueueAdapter
from .source import Source


class Corpus(QueueAdapter):


    name = 'Chadwyck Healey American Poetry'

    slug = 'chadwyck-healey-american-poetry'


    @classmethod
    def from_env(cls):

        """
        Wrap the settings-defined path.
        """

        return cls(settings.LITLAB_CHADWYCK_HEALEY_AMERICAN_POETRY)


    @classmethod
    def job(cls, corpus_id, path):

        """
        Ingest poems from a source path.

        Args:
            corpus_id (int): The id of the parent corpus.
            path (str): The path of the source file.
        """

        source = Source(path)

        for poem in source.poems():

            # Write the new text.
            text = poem.build_text(corpus_id)
            Text.objects.create(**text)


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
