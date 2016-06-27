

import os

from django.conf import settings

from .text import Text


class Corpus:


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


    def texts(self):

        """
        Generate Text instances.

        Yields: Text
        """

        for path in self.text_paths():
            yield Text(path)
