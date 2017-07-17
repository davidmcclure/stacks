#!/usr/bin/env python


from stacks.extractor import Extractor
from stacks.corpora.chadh import FictionCorpus, FictionSource


class CHADHFictionExtractor(Extractor):

    def args(self):
        """Provide a list of source paths.

        Returns: list
        """
        corpus = FictionCorpus.from_env()

        return list(corpus.source_paths())

    def flush(self, path):
        """Flush texts.

        Args:
            path (str)
        """
        source = FictionSource.from_file(path)

        rows = list(source.rows())

        self.corpus.index_rows('chadh-fiction', source.slug, *rows)


if __name__ == '__main__':
    CHADHFictionExtractor()()
