

import os

from stacks.common.singletons import config


class ExtCorpus:

    @classmethod
    def from_env(cls):

        """
        Wrap the ENV-defined root.

        Returns: cls
        """

        return cls(config['data']['ext'])

    def __init__(self, path):

        """
        Canonicalize the root path.

        Args:
            path (str)
        """

        self.path = os.path.abspath(path)

    def flush(self, text):

        """
        Write a text to disk.

        Args:
            text (dict)
        """

        pass
