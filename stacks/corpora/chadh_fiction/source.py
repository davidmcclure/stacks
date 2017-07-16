

import attr

from cached_property import cached_property
from html import unescape
from bs4 import BeautifulSoup

from stacks.utils import get_text

from .text import Text


@attr.s
class Source:

    xml = attr.ib()

    @classmethod
    def from_file(cls, path):
        """Hydrate from a file path.

        Args:
            path (str)

        Returns: cls
        """
        with open(path, 'r') as fh:
            markup = unescape(fh.read())
            return cls(BeautifulSoup(markup, 'xml'))

    def texts(self):
        """Yields: Text
        """
        for tree in self.xml.find_all('div0'):
            yield Text(tree)

    def rows(self):
        """Produce rows for each text.
        """
        for text in self.texts():
            yield text.row()

    @cached_property
    def idref(self):
        """Returns: str
        """
        # Does it work to just take the first idref?
        return get_text(self.xml, 'comhd0 idref')
