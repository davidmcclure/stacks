

import os

from bs4 import BeautifulSoup

from corpus.utils import get_text, clone_tree


class Poem:


    def __init__(self, tree):
        self.tree = tree


    @property
    def identifier(self):
        return get_text(self.tree, 'comhd3 idref')


    @property
    def source_text(self):
        return str(self.tree)


    @property
    def plain_text(self):
        return get_text(self.tree, 'l')


    @property
    def title(self):
        return get_text(self.tree, 'newatts mainhead')


    @property
    def author(self):
        return get_text(self.tree, 'somauth')


    @property
    def year(self):
        return get_text(self.tree, 'attputn1')


    def build_text(self, corpus_id):

        """
        Assemble fields for a Text instances.

        Args:
            corpus_id (int)

        Returns: dict
        """

        return dict(

            corpus_id   = corpus_id,
            identifier  = self.identifier,
            source_text = self.source_text,
            plain_text  = self.plain_text,

            title   = self.title,
            author  = self.author,
            year    = self.year,

        )
