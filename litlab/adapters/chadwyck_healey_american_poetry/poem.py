

import os

from bs4 import BeautifulSoup

from litlab.utils import get_text, clone_tree


class Poem:


    def __init__(self, tree):
        self.tree = tree


    @property
    def source_text(self):
        return str(self.tree)


    @property
    def plain_text(self):

        """
        Strip out the header metadata.

        Returns: str
        """

        copy = clone_tree(self.tree)

        # Remove metadata containers.
        for selector in ['comhd2', 'somhead', 'attribs', 'newatts']:
            tag = copy.select_one(selector)
            if tag: tag.extract()

        return get_text(copy, 'poem')


    @property
    def title(self):
        return get_text(self.tree, 'mainhead')


    @property
    def author(self):
        return get_text(self.tree, 'somauth')


    @property
    def year(self):
        return get_text(self.tree, 'attpubn1')


    @property
    def period(self):
        return get_text(self.tree, 'attperi')


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
            creator     = self.author,
            date        = self.year,
            temporal    = self.period,
            type        = self.genre,

        )
