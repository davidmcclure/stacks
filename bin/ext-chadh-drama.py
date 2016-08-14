#!/usr/bin/env python


from stacks.extractor import Extractor
from stacks.adapters.chadh_drama import Corpus, Source
from stacks.ext import corpus


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
            corpus.insert_text(play.to_json_text())


if __name__ == '__main__':
    CHADHDramaExtractor()()
