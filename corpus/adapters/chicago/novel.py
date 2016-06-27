

import os


class Novel:


    def __init__(self, corpus_path, metadata):

        """
        Store the corpus path and metadata object.

        Args:
            corpus_path (str)
            metadata (dict)
        """

        self.corpus_path = os.path.abspath(corpus_path)

        self.metadata = metadata
