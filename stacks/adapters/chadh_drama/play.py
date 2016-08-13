

import os

from bs4 import BeautifulSoup

from stacks.utils import get_text
from stacks.json_text import JSONText


class Play:

    def __init__(self, xml):

        """
        Set the XML tree.

        Args:
            xml (BeautifulSoup)
        """

        self.xml = xml

    def identifier(self):

        """
        Returns: str
        """

        return get_text(self.xml, 'idref')

    def title(self):

        """
        Returns: str
        """

        return get_text(self.xml, 'newatts atttitle')

    def author_full(self):

        """
        Returns: str
        """

        return get_text(self.xml, 'attribs attauth')

    def year(self):

        """
        Returns: int
        """

        return int(get_text(self.xml, 'newatts attpubn1'))

    def plain_text(self):

        """
        Returns: str
        """

        # TODO: Scrub out metadata.

        return ' '.join(self.xml.strings)

    def to_json_text(self):

        """
        Returns: dict
        """

        return JSONText(dict(
            corpus = 'chadh-drama',
            identifier = self.identifier(),
            title = self.title(),
            plain_text = self.plain_text(),
            author_full = self.author_full(),
            year = self.year(),
        ))
