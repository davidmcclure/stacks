#!/usr/bin/env python


from stacks.extractor import Extractor
from stacks.adapters.chadh_drama import Corpus, Source


class CHADHDramaExtractor(Extractor):

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

        source = Source(path)

        for play in source.plays():
            self.corpus.flush(play.as_ext())


if __name__ == '__main__':
    CHADHDramaExtractor()()
