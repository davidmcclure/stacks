#!/usr/bin/env python


from stacks.extractor import Extractor
from stacks.adapters.chadh_poetry import Corpus
from stacks.schemas import Text


class CHADHPoetryExtractor(Extractor):

    def args(self):

        """
        Provide a list of source paths.

        Returns: list
        """

        corpus = Corpus.from_env()

        return list(corpus.source_paths())

    def flush(self, path):

        """
        Flush texts.

        Args:
            path (str)
        """

        for text in Text.from_chadh_poetry(path):
            self.corpus.flush(text)


if __name__ == '__main__':
    CHADHPoetryExtractor()()
