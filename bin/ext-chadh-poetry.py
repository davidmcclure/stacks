#!/usr/bin/env python


from stacks.extractor import Extractor
from stacks.adapters.chadh_poetry import Corpus, Source
from stacks.ext import corpus


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

        source = Source(path)

        for poem in source.poems():
            corpus.insert_text(poem.to_json_text())


if __name__ == '__main__':
    CHADHPoetryExtractor()()
