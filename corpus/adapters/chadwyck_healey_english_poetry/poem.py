

import os

from bs4 import BeautifulSoup

from corpus.utils import get_text, remove_tags


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

        """
        Strip out the header metadata.

        Returns: str
        """

        # clean = remove_tags(self.tree, [
            # 'comhd2',
            # 'attribs',
            # 'newatts',
        # ])

        # return get_text(clean, 'poem')

        return self.tree.get_text()


    @property
    def title(self):
        return get_text(self.tree, 'newatts mainhead')


    @property
    def author(self):
        return get_text(self.tree, 'somauth')


    @property
    def year(self):
        return get_text(self.tree, 'attpubn1')


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
