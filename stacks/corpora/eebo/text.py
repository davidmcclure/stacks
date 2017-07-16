

import re
import attr
import gzip

from cached_property import cached_property
from bs4 import BeautifulSoup

from stacks.utils import get_text, try_or_log, parse_year
from stacks.models import EEBOText


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
        with gzip.open(path, 'rb') as fh:
            return cls(BeautifulSoup(fh, 'xml'))

    @cached_property
    def idno_dlps(self):
        """Returns: str
        """
        return get_text(self.xml, 'IDNO[TYPE="DLPS"]')

    @try_or_log
    def title(self):
        """Returns: str
        """
        return get_text(self.xml, 'TITLE')

    @try_or_log
    def author(self):
        """Returns: str
        """
        return get_text(self.xml, 'AUTHOR')

    @try_or_log
    def file_extent(self):
        """Returns: str
        """
        return get_text(self.xml, 'FILEDESC EXTENT')

    @try_or_log
    def file_pubplace(self):
        """Returns: str
        """
        return get_text(self.xml, 'PUBLICATIONSTMT PUBPLACE')

    @try_or_log
    def file_publisher(self):
        """Returns: str
        """
        return get_text(self.xml, 'PUBLICATIONSTMT PUBLISHER')

    @try_or_log
    def file_date(self):
        """Returns: str
        """
        return get_text(self.xml, 'PUBLICATIONSTMT DATE')

    @try_or_log
    def idno_stc(self):
        """Returns: str
        """
        return get_text(self.xml, 'IDNO[TYPE="stc"]')

    @try_or_log
    def idno_eebo_citation(self):
        """Returns: str
        """
        return get_text(self.xml, 'IDNO[TYPE="eebo citation"]')

    @try_or_log
    def idno_proquest(self):
        """Returns: str
        """
        return get_text(self.xml, 'IDNO[TYPE="proquest"]')

    @try_or_log
    def idno_vid(self):
        """Returns: str
        """
        return get_text(self.xml, 'IDNO[TYPE="vid"]')

    @try_or_log
    def source_extent(self):
        """Returns: str
        """
        return get_text(self.xml, 'SOURCEDESC EXTENT')

    @try_or_log
    def source_pubplace(self):
        """Returns: str
        """
        return get_text(self.xml, 'SOURCEDESC PUBPLACE')

    @try_or_log
    def source_publisher(self):
        """Returns: str
        """
        return get_text(self.xml, 'SOURCEDESC PUBLISHER')

    @try_or_log
    def source_date(self):
        """Returns: int
        """
        return parse_year(get_text(self.xml, 'SOURCEDESC DATE'))

    @try_or_log
    def language(self):
        """Returns: str
        """
        return get_text(self.xml, 'LANGUAGE')

    @try_or_log
    def plain_text(self):
        """Returns: str
        """
        return get_text(self.xml, 'TEXT')

    def row(self):
        """Assemble a database row.

        Returns: AmficText
        """
        return EEBOText(
            idno_dlps=self.idno_dlps,
            title=self.title(),
            author=self.author(),
            file_extent=self.file_extent(),
            file_pubplace=self.file_pubplace(),
            file_publisher=self.file_publisher(),
            file_date=self.file_date(),
            idno_stc=self.idno_stc(),
            idno_eebo_citation=self.idno_eebo_citation(),
            idno_proquest=self.idno_proquest(),
            idno_vid=self.idno_vid(),
            source_extent=self.source_extent(),
            source_pubplace=self.source_pubplace(),
            source_publisher=self.source_publisher(),
            source_date=self.source_date(),
            language=self.language(),
            text=self.plain_text(),
        )
