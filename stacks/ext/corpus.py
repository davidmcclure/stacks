

import os


class Corpus:

    def __init__(self, path):

        """
        Canonicalize the root path.

        Args:
            path (str)
        """

        self.path = os.path.abspath(path)

    def insert_text(self, text):

        """
        Write a text as compressed JSON into the corpus.

        Args:
            text (Text)
        """

        pass

    def get_text(self, corpus, identifier):

        """
        Hydrate a text instance from the JSON.

        Args:
            corpus (str)
            identifier (str)
        """

        pass

    def clear_corpus(self, corpus):

        """
        Delete a corpus directory and manifest.

        Args:
            corpus (str)
        """

        pass

    def write_manifests(self):

        """
        For each corpus, write a manifest file with relative links to each of
        the compressed JSON files.
        """

        pass
