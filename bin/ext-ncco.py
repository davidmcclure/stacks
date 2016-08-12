#!/usr/bin/env python


from stacks.extractor import Extractor
from stacks.adapters.ncco import Corpus, Text


class NCCOExtractor(Extractor):

    def args(self):

        """
        Provide a list of ECCO paths.

        Returns: list
        """

        corpus = Corpus.from_env()

        return list(corpus.text_paths())

    def flush(self, path):

        """
        Flush a text.

        Args:
            path (str)
        """

        text = Text(path)

        self.corpus.insert_text(text.as_ext())


if __name__ == '__main__':
    NCCOExtractor()()
