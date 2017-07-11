#!/usr/bin/env python


from stacks.extractor import Extractor
from stacks.corpora.gale import Corpus, Text


class GaleExtractor(Extractor):

    def args(self):
        """Provide a list of Gale paths.

        Returns: list
        """
        corpus = Corpus.from_env()

        return list(corpus.text_paths())

    def flush(self, path):
        """Flush a text.

        Args:
            path (str)
        """
        text = Text.from_file(path)

        self.corpus.index_rows('gale', text.psmid, text.row())


if __name__ == '__main__':
    GaleExtractor()()
