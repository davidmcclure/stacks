

import os

from bs4 import BeautifulSoup

from .text import Text


class Source:

    def __init__(self, path):

        """
        Parse the XML.

        Args:
            path (str): The text path.
        """

        self.path = os.path.abspath(path)

        with open(self.path, 'rb') as fh:
            self.xml = BeautifulSoup(fh, 'lxml')

    def plays(self):

        """
        Generate Poem instances.

        Yields: Poem
        """

        for tree in self.xml.find_all('div0'):
            yield Text(tree)
