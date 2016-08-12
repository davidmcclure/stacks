#!/usr/bin/env python


from stacks.extractor import Extractor
from stacks.adapters.litlab_suspense import Corpus, Text


class LitLabSuspenseExtractor(Extractor):

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

        text = Text(path)

        self.corpus.flush(text.as_ext())


if __name__ == '__main__':
    LitLabSuspenseExtractor()()
