

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
        return get_text(self.tree, 'play')


    @property
    def title(self):
        return get_text(self.tree, 'voltitle')


    @property
    def full_title(self):
        return get_text(self.tree, 'pubtitle')


    @property
    def author(self):
        return get_text(self.tree, 'volauth')


    @property
    def year(self):
        return get_text(self.tree, 'comcitn y1')


    @property
    def genre(self):
        return get_text(self.tree, 'attgenre')


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
            alternative = self.full_title,
            creator     = self.author,
            date        = self.year,
            type        = self.genre,

        )
