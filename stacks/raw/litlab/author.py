

import os

from pathlib import Path
from cached_property import cached_property

from .utils import parse_metadata


class Author:

    def __init__(self, path):

        """
        Canonicalize the author path.

        Args:
            path (str)
        """

        self.path = os.path.abspath(path)

    def metadata_path(self):

        """
        Get the path of the author's metadata file.

        Returns: str
        """

        return os.path.join(self.path, 'metadata.txt')

    @cached_property
    def metadata(self):

        """
        Parse the metadata file.

        Returns: dict
        """

        return parse_metadata(self.metadata_path())

    def folder_name(self):

        """
        Returns: str
        """

        author_dir = Path(self.path)

        return author_dir.parts[-1]

    def name_first(self):

        """
        Returns: str
        """

        return self.metadata.get('name_first')

    def name_last(self):

        """
        Returns: str
        """

        return self.metadata.get('name_last')
