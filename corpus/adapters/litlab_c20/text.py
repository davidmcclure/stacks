

import os

from slugify import slugify
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


    @property
    def author(self):

        """
        Get the parent author instance.

        Returns: Author
        """

        return Author(self.author_path)


    @property
    def metadata(self):

        """
        Parse the metadata file.

        Returns: dict
        """

        return dict(ConfigObj(self.metadata_path))


    @property
    def plain_text(self):

        """
        Read the text file.

        Returns: str
        """

        with open(self.text_path, encoding='utf8', mode='r') as fh:
            return fh.read()


    @property
    def title(self):

        """
        Get a canonicalized text title.

        Returns: str
        """

        return self.metadata['title']


    @property
    def year(self):

        """
        Get the publication year.

        Returns: int
        """

        return int(self.metadata['year'])


    @property
    def identifier(self):

        """
        Make a slug from the title.

        Returns: str
        """

        return slugify(self.title)
