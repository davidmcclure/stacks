

import re

from cached_property import cached_property

from stacks.utils import get_text, try_or_log, parse_year
from stacks.sources import XMLSource


class Text(XMLSource):

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

    @cached_property
    def idno_stc(self):
        """Returns: str
        """
        return get_text(self.xml, 'IDNO[TYPE="stc"]')

    @cached_property
    def idno_eebo_citation(self):
        """Returns: str
        """
        return get_text(self.xml, 'IDNO[TYPE="eebo citation"]')

    @cached_property
    def idno_proquest(self):
        """Returns: str
        """
        return get_text(self.xml, 'IDNO[TYPE="proquest"]')

    @cached_property
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
