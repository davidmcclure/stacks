

import os

from configobj import ConfigObj

from .author import Author


class Text:


    def __init__(self, path):

        """
        Canonicalize the text path.

        Args:
            path (str)
        """

        self.path = os.path.abspath(path)


    @property
    def author_path(self):

        """
        Get the path of the parent author.

        Returns: str
        """

        return os.path.dirname(self.path)


    @property
    def metadata_path(self):

        """
        Get the path of the text's metadata file.

        Returns: str
        """

        return os.path.join(self.path, 'metadata.txt')


    @property
    def text_path(self):

        """
        Get the path of the text file.

        Returns: str
        """

        return os.path.join(self.path, 'text.txt')


    def author(self):

        """
        Get the parent author instance.

        Returns: Author
        """

        return Author(self.author_path)


    def metadata(self):

        """
        Parse the metadata file.

        Returns: dict
        """

        return dict(ConfigObj(self.metadata_path))


    def text(self):

        """
        Read the text file.

        Returns: str
        """

        with open(self.text_path, 'r') as fh:
            return fh.read()
