

import os

from stacks.singletons import config
from stacks.utils import scan_paths


class Corpus:

    @classmethod
    def from_env(cls):

        """
        Wrap the ENV-defined directory.

        Returns: cls
        """

        path = os.path.join(config['data']['raw'], 'litlab-suspense')

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

        groups = [
            'Suspenseful',
            'Unsuspenseful',
        ]

        # Groups
        for group in groups:

            group_dir = os.path.join(self.path, group)

            # Authors
            for author_dir in next(os.walk(group_dir))[1]:

                author_path = os.path.join(group_dir, author_dir)

                # Texts
                for text_dir in next(os.walk(author_path))[1]:
                    yield os.path.join(author_path, text_dir)
