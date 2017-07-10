

import os

from cached_property import cached_property
from bs4 import BeautifulSoup

from stacks.ext import Text as ExtText
from stacks.metadata.models import ECCOText, ECCOSubjectHead
from stacks.utils import get_text


# TODO: Make generic.
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

    @cached_property
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
        return get_text(self.xml, 'notes')

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

    def text_row(self):
        """Build a text row instance.

        Returns: ECCOText
        """
        return ECCOText(
            document_id=self.document_id,
            estc_id=self.estc_id(),
            unit=self.unit(),
            reel=self.reel(),
            mcode=self.mcode(),
            pub_date=self.pub_date(),
            release_date=self.release_date(),
            source_bib_citation=self.source_bib_citation(),
            source_library=self.source_library(),
            language=self.language(),
            module=self.module(),
            document_type=self.document_type(),
            notes=self.notes(),
            author_marc_name=self.author_marc_name(),
            author_death_date=self.author_death_date(),
            author_marc_date=self.author_marc_date(),
            full_title=self.full_title(),
            display_title=self.display_title(),
            imprint_full=self.imprint_full(),
            imprint_city=self.imprint_city(),
            imprint_publisher=self.imprint_publisher(),
            imprint_year=self.imprint_year(),
            collation=self.collation(),
            publication_place=self.publication_place(),
            total_pages=self.total_pages(),
            text=self.plain_text(),
        )

    def subject_head_rows(self):
        """Build a list of subject heading rows.

        Returns: list of ECCOSubjectHead
        """
        for head in self.xml.select('locSubjectHead'):
            for subject in head.select('locSubject'):

                yield ECCOSubjectHead(
                    document_id=self.document_id,
                    type=head.attrs['type'],
                    sub_field=subject.attrs['subField'],
                    value=subject.text,
                )

    def rows(self):
        """Assemble list of all database rows.
        """
        return [self.text_row()] + list(self.subject_head_rows())
