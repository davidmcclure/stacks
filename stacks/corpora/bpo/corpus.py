

import os

from zipfile import ZipFile

from stacks import config
from stacks.utils import scan_paths


class Corpus:

    @classmethod
    def from_env(cls):
        """Wrap the ENV-defined directory.

        Returns: cls
        """
        # TODO: DRY / ENV-ify the corpus slugs?
        path = os.path.join(config['data']['raw'], 'bpo')

        return cls(path)

    def __init__(self, path):
        """Canonicalize the corpus path.

        Args:
            path (str)
        """
        self.path = os.path.abspath(path)

    def zip_paths(self):
        """Get paths to each of the .zip archives.

        Yields: str
        """
        return scan_paths(self.path, '\.zip$')

    def xml_paths(self):
        """Get (archive, path) tuples for each of the compressed XML sources.

        Yields: (str, str)
        """
        # Walk .zip files.
        for zpath in self.zip_paths():
            with ZipFile(zpath) as archive:

                # Walk zipped XML files.
                for name in archive.namelist():
                    yield (zpath, name)
