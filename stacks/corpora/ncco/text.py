
import attr

from cached_property import cached_property
from bs4 import BeautifulSoup

from stacks.utils import get_text, try_or_log, parse_8d_date
from stacks.models import NCCOText, NCCOSubjectHead


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
        with open(path, 'r') as fh:
            return cls(BeautifulSoup(fh, 'xml'))

    @cached_property
    def psmid(self):
        """Returns: str
        """
        return get_text(self.xml, 'PSMID')

    @try_or_log
    def asset_id(self):
        """Returns: str
        """
        return get_text(self.xml, 'assetID')

    @try_or_log
    def asset_id_e_toc(self):
        """Returns: str
        """
        return get_text(self.xml, 'assetIDeTOC')

    @try_or_log
    def dvi_collection_id(self):
        """Returns: str
        """
        return get_text(self.xml, 'dviCollectionID')

    @try_or_log
    def bibliographic_id(self):
        """Returns: str
        """
        return get_text(self.xml, 'bibliographicID')

    @try_or_log
    def reel(self):
        """Returns: str
        """
        return get_text(self.xml, 'reel')

    @try_or_log
    def mcode(self):
        """Returns: str
        """
        return get_text(self.xml, 'mcode')

    @try_or_log
    def ocr(self):
        """Returns: float
        """
        return float(get_text(self.xml, 'ocr'))

    @try_or_log
    def pub_date_start(self):
        """ Returns: int
        """
        return int(get_text(self.xml, 'pubDate pubDateStart')[:4])

    @try_or_log
    def pub_date_end(self):
        """ Returns: int
        """
        return int(get_text(self.xml, 'pubDate pubDateEnd')[:4])

    @try_or_log
    def release_date(self):
        """ Returns: str
        """
        return parse_8d_date(get_text(self.xml, 'releaseDate'))

    @try_or_log
    def source_library_name(self):
        """ Returns: str
        """
        return get_text(self.xml, 'sourceLibrary libraryName')

    @try_or_log
    def source_library_location(self):
        """ Returns: str
        """
        return get_text(self.xml, 'sourceLibrary libraryLocation')

    @try_or_log
    def language(self):
        """ Returns: str
        """
        return get_text(self.xml, 'language')

    @try_or_log
    def document_type(self):
        """ Returns: str
        """
        return get_text(self.xml, 'documentType')

    @try_or_log
    def notes(self):
        """ Returns: str
        """
        return get_text(self.xml, 'notes')

    @try_or_log
    def comments(self):
        """ Returns: str
        """
        return get_text(self.xml, 'comments')

    @try_or_log
    def author_composed(self):
        """ Returns: str
        """
        return get_text(self.xml, 'author composed')

    @try_or_log
    def author_first(self):
        """ Returns: str
        """
        return get_text(self.xml, 'author first')

    @try_or_log
    def author_middle(self):
        """ Returns: str
        """
        return get_text(self.xml, 'author middle')

    @try_or_log
    def author_last(self):
        """ Returns: str
        """
        return get_text(self.xml, 'author last')

    @try_or_log
    def author_birth_date(self):
        """ Returns: str
        """
        return get_text(self.xml, 'author birthDate')

    @try_or_log
    def author_death_date(self):
        """ Returns: str
        """
        return get_text(self.xml, 'author deathDate')

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
    def volume(self):
        """Returns: int
        """
        return int(get_text(self.xml, 'Volume'))

    @try_or_log
    def total_volumes(self):
        """Returns: int
        """
        return int(get_text(self.xml, 'totalVolumes'))

    @try_or_log
    def imprint_full(self):
        """Returns: str
        """
        return get_text(self.xml, 'imprintFull')

    @try_or_log
    def imprint_publisher(self):
        """Returns: str
        """
        return get_text(self.xml, 'imprintPublisher')

    @try_or_log
    def imprint_manufacture_place(self):
        """Returns: str
        """
        return get_text(self.xml, 'imprintManufacturePlace')

    @try_or_log
    def imprint_manufacturer(self):
        """Returns: str
        """
        return get_text(self.xml, 'imprintManufacturer')

    @try_or_log
    def collation(self):
        """Returns: str
        """
        return get_text(self.xml, 'collation')

    @try_or_log
    def publication_place_city(self):
        """Returns: str
        """
        return get_text(self.xml, 'publicationPlaceCity')

    @try_or_log
    def publication_place_state(self):
        """Returns: str
        """
        return get_text(self.xml, 'publicationPlaceState')

    @try_or_log
    def publication_place_country(self):
        """Returns: str
        """
        return get_text(self.xml, 'publicationPlaceCountry')

    @try_or_log
    def publication_place_composed(self):
        """Returns: str
        """
        return get_text(self.xml, 'publicationPlaceComposed')

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

        strings = [
            w.string
            for w in words
            if w.string
        ]

        return ' '.join(strings)

    def text_row(self):
        """Assemble a database row.

        Returns: AmficText
        """
        return NCCOText(
            psmid=self.psmid,
            asset_id=self.asset_id(),
            asset_id_e_toc=self.asset_id_e_toc(),
            dvi_collection_id=self.dvi_collection_id(),
            bibliographic_id=self.bibliographic_id(),
            reel=self.reel(),
            mcode=self.mcode(),
            ocr=self.ocr(),
            pub_date_start=self.pub_date_start(),
            pub_date_end=self.pub_date_end(),
            release_date=self.release_date(),
            source_library_name=self.source_library_name(),
            source_library_location=self.source_library_location(),
            language=self.language(),
            document_type=self.document_type(),
            notes=self.notes(),
            comments=self.comments(),
            author_composed=self.author_composed(),
            author_first=self.author_first(),
            author_middle=self.author_middle(),
            author_last=self.author_last(),
            author_birth_date=self.author_birth_date(),
            author_death_date=self.author_death_date(),
            full_title=self.full_title(),
            display_title=self.display_title(),
            volume=self.volume(),
            total_volumes=self.total_volumes(),
            imprint_full=self.imprint_full(),
            imprint_publisher=self.imprint_publisher(),
            imprint_manufacture_place=self.imprint_manufacture_place(),
            imprint_manufacturer=self.imprint_manufacturer(),
            collation=self.collation(),
            publication_place_city=self.publication_place_city(),
            publication_place_state=self.publication_place_state(),
            publication_place_country=self.publication_place_country(),
            publication_place_composed=self.publication_place_composed(),
            total_pages=self.total_pages(),
            text=self.plain_text(),
        )

    def subject_head_rows(self):
        """Build a list of subject heading rows.

        Returns: list of ECCOSubjectHead
        """
        for head in self.xml.select('locSubjectHead'):
            for subject in head.select('locSubject'):

                yield NCCOSubjectHead(
                    psmid=self.psmid,
                    type=head.attrs['type'],
                    sub_field=subject.attrs['subField'],
                    value=subject.text,
                )

    def rows(self):
        """Assemble list of all database rows.
        """
        return [self.text_row()] + list(self.subject_head_rows())
