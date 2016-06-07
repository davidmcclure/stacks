

import os

from corpus.adapters.litlab_c20.author import Author

from corpus.tests.adapters.mock_corpus import MockCorpus


class MockLitLabC20(MockCorpus):


    def add_author(self, dirname, name_full='McClure, David W.'):

        """
        Add an author directory to the corpus.

        Returns: Author
        """

        path = os.path.join(self.path, dirname)

        os.makedirs(path)

        # TODO: Render metadata template.

        return Author(path)
