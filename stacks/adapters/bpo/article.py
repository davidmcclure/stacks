

import os

from zipfile import ZipFile
from bs4 import BeautifulSoup

from stacks.utils import get_text


class Article:

    def __init__(self, zipfile_path, xml_name):

        """
        Extract the XML source, parse the tree.

        Args:
            zipfile_path (str)
            xml_name (str)
        """

        with ZipFile(zipfile_path) as zfile:
            with zfile.open(xml_name) as fh:
                self.xml = BeautifulSoup(fh, 'xml')

    def identifier(self):

        """
        Returns: str
        """

        return get_text(self.xml, 'RecordID')

    def title(self):

        """
        Returns: str
        """

        return get_text(self.xml, 'RecordTitle')

    def author_name_full(self):

        """
        Returns: str
        """

        return get_text(self.xml, 'Contributor OriginalForm')

    def author_name_first(self):

        """
        Returns: str
        """

        return get_text(self.xml, 'Contributor FirstName')

    def author_name_last(self):

        """
        Returns: str
        """

        return get_text(self.xml, 'Contributor LastName')

    def year(self):

        """
        Returns: int
        """

        return int(get_text(self.xml, 'NumericPubDate')[:4])

    def plain_text(self):

        """
        Returns: str
        """

        return get_text(self.xml, 'FullText')
