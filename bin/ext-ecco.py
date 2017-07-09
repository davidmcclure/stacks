#!/usr/bin/env python


from stacks.extractor import Extractor
from stacks.raw import ecco


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

        rows = text.rows()

        self.corpus.index_rows('ecco', rows)


if __name__ == '__main__':
    ECCOExtractor()()
