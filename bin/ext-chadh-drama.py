#!/usr/bin/env python


from stacks.extractor import Extractor
from stacks.raw.chadh_drama import Corpus, Source


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

        # TODO: Wrap each insert in a try/except?

        for play in source.plays():
            self.corpus.insert_text(play.to_ext_text())


if __name__ == '__main__':
    CHADHDramaExtractor()()
