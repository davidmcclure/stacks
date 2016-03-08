

import glob
import os

from litlab.conf import settings

from .text import Text


class Corpus:


    @classmethod
    def from_env(cls):

        """
        Wrap the settings-defined path.
        """

        return cls(settings.LITLAB_CHADH_ENGLISH_DRAMA)


    def __init__(self, path):

        """
        Set the corpus path.

        Args:
            path (str): The corpus path.
        """

        self.path = os.path.abspath(path)


    def __iter__(self):

        """
        Generate text text metadata.

        Yields:
            dict: Properties for the each text.
        """

        for path in glob.glob(os.path.join(self.path, '*.new')):
            yield Text(path).row
