#!/usr/bin/env python


from stacks.extractor import Extractor
from stacks.corpora.chadh_drama import Corpus, Source


class CHADHDramaExtractor(Extractor):

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
        source = Source.from_file(path)

        rows = list(source.rows())

        self.corpus.index_rows('chadh-drama', source.slug, *rows)


if __name__ == '__main__':
    CHADHDramaExtractor()()
