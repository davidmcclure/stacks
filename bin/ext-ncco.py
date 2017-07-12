#!/usr/bin/env python


from stacks.extractor import Extractor
from stacks.corpora.ncco import Corpus, Text


class NCCOExtractor(Extractor):

    def args(self):
        """Provide a list of ECCO paths.

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

        self.corpus.index_rows('ncco', text.psmid, text.row())


if __name__ == '__main__':
    NCCOExtractor()()
