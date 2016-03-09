

import glob
import os

from litlab.conf import settings

from corpora.models import Text
from corpora.adapters import QueueAdapter
from .volume import Volume


class ChadwyckHealeyEnglishDrama(QueueAdapter):


    name = 'Chadwyck Healey English Drama'

    slug = 'chadwyck-healey-english-drama'


    @classmethod
    def from_env(cls):

        """
        Wrap the settings-defined path.
        """

        return cls(settings.LITLAB_CHADH_ENG_DRAMA)


    @classmethod
    def job(cls, corpus_id, path):

        """
        Add an individual text.

        Args:
            corpus_id (int): The id of the parent corpus.
            path (str): The path of the XML file.
        """

        volume = Volume(path)

        # Write the new text.
        row = volume.build_row(corpus_id)
        Text.objects.create(**row)


    def __init__(self, path):

        """
        Set the corpus path.

        Args:
            path (str): The corpus path.
        """

        self.path = os.path.abspath(path)


    @property
    def paths(self):

        """
        Generate text paths.

        Yields:
            str: The next path
        """

        return glob.glob(os.path.join(self.path, '*.new'))
