

import os

from bs4 import BeautifulSoup

from stacks.utils import get_text


class Text:

    def __init__(self, path):

        """
        Parse the XML.

        Args:
            path (str)
        """

        self.path = os.path.abspath(path)

        with open(self.path, 'rb') as fh:
            self.xml = BeautifulSoup(fh, 'xml')

    def identifier(self):

        """
        Returns: str
        """

        return get_text(self.xml, 'documentID')

    def title(self):

        """
        Returns: str
        """

        return get_text(self.xml, 'fullTitle')

    def author_marc_name(self):

        """
        Returns: str
        """

        return get_text(self.xml, 'author marcName')

    def year(self):

        """
        Returns: int
        """

        return int(get_text(self.xml, 'pubDate')[:4])

    def plain_text(self):

        """
        Returns: str
        """

        words = self.xml.select('wd')

        strings = [w.string for w in words]

        return ' '.join(strings)
