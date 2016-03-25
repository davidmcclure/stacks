

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
        for tag in ['comhd3', 'attribs', 'newatts']:
            copy.select_one(tag).extract()

        return get_text(copy, 'poem')


    @property
    def title(self):
        return get_text(self.tree, 'mainhead')


    @property
    def author(self):
        return get_text(self.tree, 'somauth')


    @property
    def genre(self):
        return get_text(self.tree, 'attgenre')
