#!/usr/bin/env python


from stacks.extractor import Extractor
from stacks.adapters.price_lab import Corpus, Text


class PriceLabExtractor(Extractor):

    def args(self):

        """
        Provide a list of source args.

        Returns: list
        """

        corpus = Corpus.from_env()

        return [
            dict(texts_path=corpus.path, metadata=row)
            for row in corpus.metadata()
        ]

    def flush(self, *args, **kwargs):

        """
        Flush text.
        """

        text = Text(*args, **kwargs)

        self.corpus.insert_text(text.as_ext())


if __name__ == '__main__':
    PriceLabExtractor()()
