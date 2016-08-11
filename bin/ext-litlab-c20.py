#!/usr/bin/env python


from stacks.extractor import Extractor
from stacks.adapters.litlab_c20 import Corpus
from stacks.schemas import Text


class LitLabC20Extractor(Extractor):

    def args(self):

        """
        Provide a list of source paths.

        Returns: list
        """

        corpus = Corpus.from_env()

        return list(corpus.text_paths())

    def flush(self, path):

        """
        Flush a text.

        Args:
            path (str)
        """

        text = Text.from_litlab_c20(path)

        self.corpus.flush(text)


if __name__ == '__main__':
    LitLabC20Extractor()()
