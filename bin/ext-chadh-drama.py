#!/usr/bin/env python


from stacks.extractor import Extractor
from stacks.adapters.chadh_drama import Corpus
from stacks.schemas import Text


class CHADHDramaExtractor(Extractor):

    def args(self):

        """
        Provide a list Chadwyck Healey source paths.

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

        for text in Text.from_chadh_drama(path):
            self.corpus.flush(text)


if __name__ == '__main__':
    CHADHDramaExtractor()()
