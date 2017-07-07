

import os

from bs4 import BeautifulSoup

from stacks.ext import Text as ExtText
from stacks.utils import get_text


class XMLSource:

    @classmethod
    def from_file(cls, path):
        """Hydrate from a file path.

        Args:
            path (str)

        Returns: cls
        """
        with open(path, 'rb') as fh:
            return cls(BeautifulSoup(fh, 'xml'))

    def __init__(self, xml):
        self.xml = xml


class Text(XMLSource):

    def identifier(self):
        """Returns: str
        """
        return get_text(self.xml, 'documentID')

    def title(self):
        """Returns: str
        """
        return get_text(self.xml, 'fullTitle')

    def author_marc_name(self):
        """Returns: str
        """
        return get_text(self.xml, 'author marcName')

    def year(self):
        """Returns: int
        """
        return int(get_text(self.xml, 'pubDate')[:4])

    def plain_text(self):
        """Returns: str
        """
        words = self.xml.select('wd')

        strings = [w.string for w in words]

        return ' '.join(strings)

    def to_ext_text(self):
        """Returns: dict
        """
        return ExtText(dict(
            corpus = 'ecco',
            identifier = self.identifier(),
            title = self.title(),
            plain_text = self.plain_text(),
            author_full = self.author_marc_name(),
            year = self.year(),
        ))
