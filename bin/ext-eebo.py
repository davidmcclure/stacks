#!/usr/bin/env python


from stacks.extractor import Extractor
from stacks.adapters.eebo import Corpus
from stacks.schemas import Text


class EEBOExtractor(Extractor):

    def args(self):

        """
        Provide a list of source paths.

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

        text = Text.from_eebo(path)

        self.corpus.flush(text)


if __name__ == '__main__':
    EEBOExtractor()()
