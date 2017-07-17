

import attr
import os

from cached_property import cached_property
from bs4 import BeautifulSoup

from stacks.utils import get_text

from .text import Text


@attr.s
class Source:

    slug = attr.ib()

    xml = attr.ib()

    @classmethod
    def from_file(cls, path):
        """Hydrate from a file path.

        Args:
            path (str)

        Returns: cls
        """
        slug = os.path.splitext(os.path.basename(path))[0]

        with open(path, 'r') as fh:
            return cls(slug, BeautifulSoup(fh, 'lxml'))

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
