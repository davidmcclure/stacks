

import os

from bs4 import BeautifulSoup

from stacks.sources import XMLSource

from .text import Text


class Source(XMLSource):

    def texts(self):
        """Yields: Text
        """
        for tree in self.xml.find_all('div0'):
            yield Text(tree)
