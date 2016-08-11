#!/usr/bin/env python


from stacks.extractor import Extractor
from stacks.adapters.dime_westerns import Corpus
from stacks.schemas import Text


class DimeWesternsExtractor(Extractor):

    def args(self):

        """
        Provide a list of source paths.

        Returns: list
        """

        corpus = Corpus.from_env()

        return [

            dict(
                texts_path=corpus.texts_path(),
                slug=slug,
                metadata=row,
            )

            for slug, row in corpus.metadata()

        ]

    def flush(self, *args, **kwargs):

        """
        Flush texts.
        """

        text = Text.from_dime_westerns(*args, **kwargs)

        self.corpus.flush(text)


if __name__ == '__main__':
    DimeWesternsExtractor()()
