

import re
import attr

from bs4 import BeautifulSoup
from cached_property import cached_property

from stacks.utils import get_text, try_or_log, parse_8d_date
from stacks.models import ECCOText, ECCOSubjectHead


@attr.s
class Text:

    xml = attr.ib()

    @classmethod
    def from_file(cls, path):
        """Hydrate from a file path.

        Args:
            path (str)

        Returns: cls
        """
        with open(path, 'rb') as fh:
            return cls(BeautifulSoup(fh, 'xml'))

    @cached_property
    def document_id(self):
        """Returns: str
        """
        return get_text(self.xml, 'documentID')

    @try_or_log
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

    @try_or_log
    def mcode(self):
        """Returns: str
        """
        return get_text(self.xml, 'mcode')

    @try_or_log
    def pub_date(self):
        """Returns: date
        """
        return parse_8d_date(get_text(self.xml, 'pubDate'))

    @try_or_log
    def release_date(self):
        """Returns: date
        """
        return parse_8d_date(get_text(self.xml, 'releaseDate'))

    @try_or_log
    def source_bib_citation(self):
        """Returns: str
        """
        return get_text(self.xml, 'sourceBibCitation')

    @try_or_log
    def source_library(self):
        """Returns: str
        """
        return get_text(self.xml, 'sourceLibrary')

    @try_or_log
    def language(self):
        """Returns: str
        """
        return get_text(self.xml, 'language')

    @try_or_log
    def module(self):
        """Returns: str
        """
        return get_text(self.xml, 'module')

    @try_or_log
    def document_type(self):
        """Returns: str
        """
        return get_text(self.xml, 'documentType')

    @try_or_log
    def notes(self):
        """Returns: str
        """
        return get_text(self.xml, 'notes')

    @try_or_log
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

    @try_or_log
    def author_marc_date(self):
        """Returns: str
        """
        return get_text(self.xml, 'author marcDate')

    @try_or_log
    def full_title(self):
        """Returns: str
        """
        return get_text(self.xml, 'fullTitle')

    @try_or_log
    def display_title(self):
        """Returns: str
        """
        return get_text(self.xml, 'displayTitle')

    @try_or_log
    def imprint_full(self):
        """Returns: str
        """
        return get_text(self.xml, 'imprintFull')

    @try_or_log
    def imprint_city(self):
        """Returns: str
        """
        return get_text(self.xml, 'imprintCity')

    @try_or_log
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

    @try_or_log
    def collation(self):
        """Returns: str
        """
        return get_text(self.xml, 'collation')

    @try_or_log
    def publication_place(self):
        """Returns: str
        """
        return get_text(self.xml, 'publicationPlace')

    @try_or_log
    def total_pages(self):
        """Returns: int
        """
        return int(get_text(self.xml, 'totalPages'))

    @try_or_log
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
