

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

    def document_id(self):
        """Returns: str
        """
        return get_text(self.xml, 'documentID')

    def full_title(self):
        """Returns: str
        """
        return get_text(self.xml, 'fullTitle')

    def author_marc_name(self):
        """Returns: str
        """
        return get_text(self.xml, 'author marcName')

    def pub_date(self):
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
            identifier = self.document_id(),
            title = self.full_title(),
            plain_text = self.plain_text(),
            author_full = self.author_marc_name(),
            year = self.pub_date(),
        ))
