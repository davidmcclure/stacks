#!/usr/bin/env python


from stacks.extractor import Extractor
from stacks.corpora import ecco


class ECCOExtractor(Extractor):

    def args(self):
        """Provide a list of ECCO paths.

        Returns: list
        """
        corpus = ecco.Corpus.from_env()

        return list(corpus.text_paths())

    def flush(self, path):
        """Flush a text.

        Args:
            path (str)
        """
        text = ecco.Text.from_file(path)

        self.corpus.index_rows('ecco', text.document_id, *text.rows())


if __name__ == '__main__':
    ECCOExtractor()()
