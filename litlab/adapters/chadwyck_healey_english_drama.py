

import os
import glob

from bs4 import BeautifulSoup

from litlab.utils import get_text
from litlab.conf import settings



class Corpus:


    @classmethod
    def from_env(cls):

        """
        Wrap the settings-defined path.
        """

        return cls(settings.LITLAB_CHADH_ENGLISH_DRAMA)


    def __init__(self, path):

        """
        Set the corpus path.

        Args:
            path (str): The corpus path.
        """

        self.path = os.path.abspath(path)


    def texts(self):

        """
        Generate text text metadata.

        Yields:
            dict: Properties for the each text.
        """

        for path in glob.glob(os.path.join(self.path, '*.new')):
            yield Text(path)



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
