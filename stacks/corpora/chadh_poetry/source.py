

import attr
import os

from cached_property import cached_property
from html import unescape
from bs4 import BeautifulSoup

from stacks.utils import get_text

from .poem import Poem


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

        with open(path, 'rb') as fh:
            return cls(slug, BeautifulSoup(fh, 'lxml'))

    def poems(self):
        """Yields: Text
        """
        for tree in self.xml.find_all('poem'):
            yield Poem(tree)

    def rows(self):
        """Produce rows for each poem.
        """
        for poem in self.poems():
            yield poem.row()
