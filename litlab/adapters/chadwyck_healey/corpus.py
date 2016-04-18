

import glob
import os

from corpora.adapters import QueueAdapter


class Corpus(QueueAdapter):


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
