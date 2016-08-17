#!/usr/bin/env python


from stacks.extractor import Extractor
from stacks.raw.litlab_c20 import Corpus, Text


class LitLabC20Extractor(Extractor):

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

        self.corpus.insert_text(text.to_ext_text())


if __name__ == '__main__':
    ext = LitLabC20Extractor()
    ext.run()
