

import os

from configobj import ConfigObj


class Author:


    def __init__(self, path):

        """
        Canonicalize the author path.

        Args:
            path (str)
        """

        self.path = os.path.abspath(path)


    @property
    def metadata_path(self):

        """
        Get the path of the author's metadata file.

        Returns: str
        """

        return os.path.join(self.path, 'metadata.txt')


    def metadata(self):

        """
        Parse the metadata file.

        Returns: dict
        """

        return dict(ConfigObj(self.metadata_path))


    def name_full(self):

        """
        Get the author's full name as a single string.

        Returns: str
        """

        return ', '.join(self.metadata['name_full'])
