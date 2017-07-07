

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

    def estc_id(self):
        """Returns: str
        """
        return get_text(self.xml, 'ESTCID')

    def unit(self):
        """Returns: int
        """
        return int(get_text(self.xml, 'unit'))

    def reel(self):
        """Returns: int
        """
        return int(get_text(self.xml, 'reel'))

    def mcode(self):
        """Returns: str
        """
        return get_text(self.xml, 'mcode')

    # TODO: Parse date.
    def pub_date(self):
        """Returns: int
        """
        return int(get_text(self.xml, 'pubDate')[:4])

    # TODO: Parse date.
    def release_date(self):
        """Returns: int
        """
        return int(get_text(self.xml, 'releaseDate')[:4])

    def source_bib_citation(self):
        """Returns: str
        """
        return get_text(self.xml, 'sourceBibCitation')

    def source_library(self):
        """Returns: str
        """
        return get_text(self.xml, 'sourceLibrary')

    def language(self):
        """Returns: str
        """
        return get_text(self.xml, 'language')

    def module(self):
        """Returns: str
        """
        return get_text(self.xml, 'module')

    def document_type(self):
        """Returns: str
        """
        return get_text(self.xml, 'documentType')

    def notes(self):
        """Returns: str
        """
        return get_text(self.xml, 'nodes')

    def author_marc_name(self):
        """Returns: str
        """
        return get_text(self.xml, 'author marcName')

    def author_death_date(self):
        """Returns: int
        """
        return int(get_text(self.xml, 'author deathDate'))

    def author_marc_date(self):
        """Returns: str
        """
        return get_text(self.xml, 'author marcDate')

    def full_title(self):
        """Returns: str
        """
        return get_text(self.xml, 'fullTitle')

    def display_title(self):
        """Returns: str
        """
        return get_text(self.xml, 'displayTitle')

    def imprint_full(self):
        """Returns: str
        """
        return get_text(self.xml, 'imprintFull')

    def imprint_city(self):
        """Returns: str
        """
        return get_text(self.xml, 'imprintCity')

    def imprint_publisher(self):
        """Returns: str
        """
        return get_text(self.xml, 'imprintPublisher')

    def imprint_year(self):
        """Returns: str
        """
        return get_text(self.xml, 'imprintYear')

    def collation(self):
        """Returns: str
        """
        return get_text(self.xml, 'collation')

    def publication_place(self):
        """Returns: str
        """
        return get_text(self.xml, 'publicationPlace')

    def total_pages(self):
        """Returns: int
        """
        return int(get_text(self.xml, 'totalPages'))

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
