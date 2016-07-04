

import os

from bs4 import BeautifulSoup

from .poem import Poem


class Source:

    def __init__(self, path):

        """
        Parse the XML.

        Args:
            path (str): The text path.
        """

        self.path = os.path.abspath(path)

        with open(self.path, 'rb') as fh:
            self.xml = BeautifulSoup(fh, 'xml')

    def poems(self):

        """
        Yields: Poem
        """

        for tree in self.xml.find_all('poem'):
            yield Poem(tree)
