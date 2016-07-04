

import os

from bs4 import BeautifulSoup

from .play import Play


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
        Yields: Play
        """

        for tree in self.xml.find_all('div0'):
            yield Play(tree)
