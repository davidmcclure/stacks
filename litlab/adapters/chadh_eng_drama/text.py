

import os

from bs4 import BeautifulSoup

from litlab.utils import get_text


class Text:


    def __init__(self, path):

        """
        Parse the XML.

        Args:
            path (str): The text path.
        """

        self.path = os.path.abspath(path)

        with open(self.path, 'rb') as fh:
            self.xml = BeautifulSoup(fh, 'lxml')


    @property
    def source_text(self):

        """
        Get the raw markup as a string.

        Returns: str
        """

        return str(self.xml)


    @property
    def plain_text(self):

        """
        Extract plaintext.

        Returns: str
        """

        return get_text(self.xml, 'play')


    @property
    def title(self):

        """
        Query the title.

        Returns: str
        """

        return get_text(self.xml, 'voltitle')


    @property
    def author(self):

        """
        Query the author.

        Returns: str
        """

        return get_text(self.xml, 'volauth')


    @property
    def build_row(self, corpus_id):

        """
        Assemble columns for a Text instances.

        Args:
            corpus_id (int)

        Returns: dict
        """

        return dict(
            corpus      = corpus_id,
            plain_text  = self.plain_text,
            source_text = self.source_text,
            title       = self.title,
            creator     = self.author,
        )
