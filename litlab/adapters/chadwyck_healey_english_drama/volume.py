

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

        """
        Get the raw markup as a string.

        Returns: str
        """

        return str(self.tree)


    @property
    def plain_text(self):

        """
        Extract plaintext.

        Returns: str
        """

        return get_text(self.tree, 'play')


    @property
    def title(self):

        """
        Query the title.

        Returns: str
        """

        return get_text(self.tree, 'voltitle')


    @property
    def author(self):

        """
        Query the author.

        Returns: str
        """

        return get_text(self.tree, 'volauth')


    def build_text(self, corpus_id):

        """
        Assemble fields for a Text instances.

        Args:
            corpus_id (int)

        Returns: dict
        """

        return dict(
            corpus_id   = corpus_id,
            plain_text  = self.plain_text,
            source_text = self.source_text,
            title       = self.title,
            creator     = self.author,
        )
