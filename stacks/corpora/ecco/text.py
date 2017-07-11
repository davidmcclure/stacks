

import os
import attr
import re

from datetime import datetime as dt

from cached_property import cached_property
from bs4 import BeautifulSoup

from stacks.utils import get_text, try_or_log
from stacks.sources import XMLSource
from stacks.models import ECCOText, ECCOSubjectHead

# from .utils import parse_date


def parse_date(text):
    """Parse an ECCO date string.
    """
    return dt.strptime(text, '%Y%m%d').date()


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

    @try_or_log
    def unit(self):
        """Returns: int
        """
        return int(get_text(self.xml, 'unit'))

    @try_or_log
    def reel(self):
        """Returns: int
        """
        return int(get_text(self.xml, 'reel'))

    def mcode(self):
        """Returns: str
        """
        return get_text(self.xml, 'mcode')

    def pub_date(self):
        """Returns: date
        """
        return parse_date(get_text(self.xml, 'pubDate'))

    def release_date(self):
        """Returns: date
        """
        return parse_date(get_text(self.xml, 'releaseDate'))

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

    @try_or_log
    def author_birth_date(self):
        """Returns: int
        """
        return int(get_text(self.xml, 'author birthDate'))

    @try_or_log
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

    @try_or_log
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

    @try_or_log
    def imprint_year(self):
        """Returns: str
        """
        text = get_text(self.xml, 'imprintYear')
        return int(re.match('[0-9]{4}', text).group(0))

    def collation(self):
        """Returns: str
        """
        return get_text(self.xml, 'collation')

    def publication_place(self):
        """Returns: str
        """
        return get_text(self.xml, 'publicationPlace')

    @try_or_log
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
            author_birth_date=self.author_birth_date(),
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
