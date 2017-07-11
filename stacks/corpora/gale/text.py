

import os

from bs4 import BeautifulSoup
from cached_property import cached_property

from stacks.utils import get_text
from stacks.sources import XMLSource
from stacks.models import GaleText


class Text(XMLSource):

    @cached_property
    def psmid(self):
        """Returns: str
        """
        return get_text(self.xml, 'PSMID')

    def full_title(self):
        """Returns: str
        """
        return get_text(self.xml, 'titleGroup fullTitle')

    def author_composed(self):
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

    def pub_date_start(self):
        """ Returns: int
        """
        return parse_date(get_text(self.xml, 'pubDate pubDateStart'))

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

    def row(self):
        """Assemble a database row.

        Returns: GaleText
        """
        return GaleText(
            psmid=self.psmid(),
            pub_date_start=self.pub_date_start(),
            author_composed=self.author_composed(),
            author_first=self.author_first(),
            author_last=self.author_last(),
            full_title=self.full_title(),
            text=self.plain_text(),
        )
