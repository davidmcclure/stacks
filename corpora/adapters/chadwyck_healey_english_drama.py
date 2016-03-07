

import os


class Corpus:


    @classmethod
    def from_env(cls):

        """
        Get an instance for the settings-defined corpus.
        """

        # TODO
        return cls()


    def __init__(self, path):

        """
        Set the corpus path.
        """

        self.path = os.path.abspath(path)
