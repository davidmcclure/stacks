

import os

from pathlib import Path
from cached_property import cached_property
from configobj import ConfigObj


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

        return dict(ConfigObj(self.metadata_path()))


    def folder_name(self):

        """
        Get the author's full name.

        Returns: str
        """

        author_dir = Path(self.path)

        return author_dir.parts[-1]
