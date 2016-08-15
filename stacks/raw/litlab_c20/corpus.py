

import os

from stacks import config


class Corpus:

    @classmethod
    def from_env(cls):

        """
        Wrap the ENV-defined directory.

        Returns: cls
        """

        path = os.path.join(config['data']['raw'], 'litlab-c20')

        return cls(path)

    def __init__(self, path):

        """
        Canonicalize the corpus path.

        Args:
            path (str)
        """

        self.path = os.path.abspath(path)

    def text_paths(self):

        """
        Generate a path for each text directory.

        Yields: str
        """

        for author_dir in next(os.walk(self.path))[1]:

            # Get the full author path.
            author_path = os.path.join(self.path, author_dir)

            for text_dir in next(os.walk(author_path))[1]:

                # Yield each text path.
                yield os.path.join(author_path, text_dir)
