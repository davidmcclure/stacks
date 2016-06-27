

import os

from configobj import ConfigObj
from cached_property import cached_property
from slugify import slugify

from .author import Author


class Text:


    def __init__(self, path):

        """
        Canonicalize the text path.

        Args:
            path (str)
        """

        self.path = os.path.abspath(path)


    def author_path(self):

        """
        Get the path of the parent author.

        Returns: str
        """

        return os.path.dirname(self.path)


    def metadata_path(self):

        """
        Get the path of the text's metadata file.

        Returns: str
        """

        return os.path.join(self.path, 'metadata.txt')


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

        return Author(self.author_path())


    @cached_property
    def metadata(self):

        """
        Parse the metadata file.

        Returns: dict
        """

        return dict(ConfigObj(self.metadata_path(), list_values=False))


    def plain_text(self):

        """
        Read the text file.

        Returns: str
        """

        with open(
            self.text_path(),
            mode='r',
            encoding='utf8',
            errors='ignore'
        ) as fh:

            return fh.read()


    def title(self):

        """
        Get a canonicalized text title.

        Returns: str
        """

        return self.metadata['title']


    def year(self):

        """
        Get the publication year.

        Returns: int
        """

        # Split year ranges into arrays.
        years = self.metadata['year'].split('-')

        # TODO: Store start + end year?
        return int(years[0])


    def identifier(self):

        """
        Make a slug from the author + title.

        Returns: str
        """

        return slugify(' '.join([
            self.author.name_full(),
            self.title(),
        ]))
