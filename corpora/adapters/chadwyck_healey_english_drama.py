

import os


class Corpus:


    @classmethod
    def from_env(cls):

        """
        Get an instance for the settings-defined corpus.
        """

        return cls(settings.CHADWYCK_HEALEY_ENGLISH_DRAMA_PATH)


    def __init__(self, path):

        """
        Set the corpus path.
        """

        self.path = os.path.abspath(path)
