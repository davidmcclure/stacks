

import os

from litlab.conf import settings


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
        """

        self.path = os.path.abspath(path)
