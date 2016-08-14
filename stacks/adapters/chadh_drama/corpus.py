

import os
import scandir

from stacks import config
from stacks.utils import scan_paths


class Corpus:

    @classmethod
    def from_env(cls):

        """
        Wrap the ENV-defined directory.

        Returns: cls
        """

        path = os.path.join(config['data']['raw'], 'chadh-drama')

        return cls(path)

    def __init__(self, path):

        """
        Canonicalize the corpus path.

        Args:
            path (str)
        """

        self.path = os.path.abspath(path)

    def source_paths(self):

        """
        Generate paths to the XML sources.

        Yields: str
        """

        return scan_paths(self.path, '\.new$')
