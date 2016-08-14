#!/usr/bin/env python


from stacks.extractor import Extractor
from stacks.adapters.ecco import Corpus, Text
from stacks.ext import corpus


class ECCOExtractor(Extractor):

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

        corpus.insert_text(text.to_json_text())


if __name__ == '__main__':
    ECCOExtractor()()
