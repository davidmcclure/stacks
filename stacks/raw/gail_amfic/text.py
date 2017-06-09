

import os

from bs4 import BeautifulSoup

from stacks.ext import Text as ExtText
from stacks.utils import get_text


class Text:

    def __init__(self, path):
        """Parse the XML.

        Args:
            path (str)
        """
        self.path = os.path.abspath(path)

        with open(self.path, 'rb') as fh:
            self.xml = BeautifulSoup(fh, 'xml')

    def identifier(self):
        """Returns: str
        """
        return get_text(self.xml, 'PSMID')

    def title(self):
        """Returns: str
        """
        return get_text(self.xml, 'titleGroup fullTitle')

    def author_full(self):
        """Returns: str
        """
        return get_text(self.xml, 'author composed')

    def author_first(self):
        """Returns: str
        """
        return get_text(self.xml, 'author first')

    def author_last(self):
        """Returns: str
        """
        return get_text(self.xml, 'author last')

    def year(self):
        """ Returns: int
        """
        return int(get_text(self.xml, 'pubDate pubDateStart')[:4])

    def plain_text(self):
        """Returns: str
        """
        words = self.xml.select('wd')

        strings = [
            w.string
            for w in words
            if w.string
        ]

        return ' '.join(strings)

    def to_ext_text(self):
        """Returns: dict
        """
        return ExtText(dict(
            corpus = 'gail-amfic',
            identifier = self.identifier(),
            title = self.title(),
            plain_text = self.plain_text(),
            author_full = self.author_full(),
            author_first = self.author_first(),
            author_last = self.author_last(),
            year = self.year(),
        ))
