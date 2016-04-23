

import glob
import os

from litlab.conf import settings

from corpus.models import Text
from corpus.adapters import QueueAdapter
from .source import Source


class Corpus(QueueAdapter):


    name = 'Chadwyck Healey American Drama'

    slug = 'chadwyck-healey-american-drama'


    @classmethod
    def from_env(cls):

        """
        Wrap the settings-defined path.
        """

        return cls(settings.LITLAB_CHADWYCK_HEALEY_AMERICAN_DRAMA)


    @classmethod
    def job(cls, corpus_id, path):

        """
        Ingest volumes from a source path.

        Args:
            corpus_id (int): The id of the parent corpus.
            path (str): The path of the source file.
        """

        source = Source(path)

        for volume in source.volumes():

            # Write the new text.
            text = volume.build_text(corpus_id)
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
