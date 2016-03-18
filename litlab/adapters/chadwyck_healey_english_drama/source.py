

import os

from bs4 import BeautifulSoup

from .volume import Volume


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


    def volumes(self):

        """
        Generate Volume instances.

        Yields: Volume
        """

        for tree in self.xml.find_all('div0'):
            yield Volume(tree)
