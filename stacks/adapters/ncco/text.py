

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

        return get_text(self.xml, 'PSMID')

    def title(self):

        """
        Returns: str
        """

        return get_text(self.xml, 'titleGroup fullTitle')

    def author_name_full(self):

        """
        Returns: str
        """

        return get_text(self.xml, 'author composed')

    def author_name_first(self):

        """
        Returns: str
        """

        return get_text(self.xml, 'author first')

    def author_name_last(self):

        """
        Returns: str
        """

        return get_text(self.xml, 'author last')

    def year(self):

        """
        Returns: int
        """

        return int(get_text(self.xml, 'pubDate year'))

    def plain_text(self):

        """
        Returns: str
        """

        words = self.xml.select('wd')

        strings = [
            w.string
            for w in words
            if w.string
        ]

        return ' '.join(strings)

    def as_ext(self):

        """
        Returns: dict
        """

        return dict(
            corpus = 'ncco',
            identifier = self.identifier(),
            title = self.title(),
            plain_text = self.plain_text(),
            author_name_full = self.author_name_full(),
            year = self.year(),
        )
