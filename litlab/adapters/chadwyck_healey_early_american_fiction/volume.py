

import os

from bs4 import BeautifulSoup

from litlab.utils import get_text


class Volume:


    def __init__(self, tree):

        """
        Set the source tree.

        Args:
            tree (BeautifulSoup): The parent <div0>.
        """

        self.tree = tree


    @property
    def source_text(self):
        return str(self.tree)


    @property
    def plain_text(self):
        return get_text(self.tree, 'doc')


    @property
    def title(self):
        return get_text(self.tree, 'voltitle')


    @property
    def author(self):
        return get_text(self.tree, 'volauth')


    @property
    def year(self):
        return get_text(self.tree, 'comcitn y1')


    def build_text(self, corpus_id):

        """
        Assemble fields for a Text instances.

        Args:
            corpus_id (int)

        Returns: dict
        """

        return dict(

            corpus_id   = corpus_id,
            source_text = self.source_text,
            plain_text  = self.plain_text,

            title       = self.title,
            creator     = self.author,
            date        = self.year,

        )
