

import os
import gzip

from bs4 import BeautifulSoup

from stacks.utils import get_text
from stacks.json_text import JSONText


class Text:

    def __init__(self, path):

        """
        Parse the XML.

        Args:
            path (str)
        """

        self.path = os.path.abspath(path)

        with gzip.open(self.path, 'rb') as fh:
            self.xml = BeautifulSoup(fh, 'xml')

    def identifier(self):

        """
        Returns: str
        """

        return get_text(self.xml, 'IDNO[TYPE="DLPS"]')

    def title(self):

        """
        Returns: str
        """

        return get_text(self.xml, 'TITLE')

    def author(self):

        """
        Returns: str
        """

        return get_text(self.xml, 'AUTHOR')

    def year(self):

        """
        Returns: int
        """

        return int(get_text(self.xml, 'SOURCEDESC DATE')[:4])

    def plain_text(self):

        """
        Returns: str
        """

        return get_text(self.xml, 'TEXT')

    def to_json_text(self):

        """
        Returns: dict
        """

        return JSONText(dict(
            corpus = 'eebo',
            identifier = self.identifier(),
            title = self.title(),
            plain_text = self.plain_text(),
            author_name_full = self.author(),
            year = self.year(),
        ))
