#!/usr/bin/env python


from stacks.extractor import Extractor
from stacks.raw.chadh_poetry import Corpus, Source


class CHADHPoetryExtractor(Extractor):

    def args(self):
        """Provide a list of source paths.

        Returns: list
        """
        corpus = Corpus.from_env()

        return list(corpus.source_paths())

    def flush(self, path):
        """Flush texts.

        Args:
            path (str)
        """
        source = Source(path)

        for poem in source.poems():
            self.corpus.insert_text(poem.to_ext_text())


if __name__ == '__main__':
    CHADHPoetryExtractor()()
