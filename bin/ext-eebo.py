#!/usr/bin/env python


from stacks.extractor import Extractor
from stacks.corpora.eebo import Corpus, Text


class EEBOExtractor(Extractor):

    def args(self):
        """Provide a list of source paths.

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

        self.corpus.index_rows('eebo', text.idno_dlps, text.row())


if __name__ == '__main__':
    EEBOExtractor()()
