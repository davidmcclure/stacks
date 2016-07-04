

import os

from bs4 import BeautifulSoup

from corpus.utils import get_text


class Text:

    def __init__(self, xml):

        """
        Set the XML tree.

        Args:
            xml (BeautifulSoup)
        """

        self.xml = xml

    def identifier(self):

        """
        Returns: str
        """

        return get_text(self.xml, 'idref')

    def title(self):

        """
        Returns: str
        """

        return get_text(self.xml, 'newatts atttitle')

    def author_name_full(self):

        """
        Returns: str
        """

        return (
            get_text(self.xml, 'attribs attauth') or
            get_text(self.xml, 'a1')
        )

    def year(self):

        """
        Returns: int
        """

        return int(get_text(self.xml, 'newatts attpubn1'))

    def plain_text(self):

        """
        Returns: str
        """

        # TODO: Scrub out metadata.

        return ' '.join(self.xml.strings)
