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

    def flush(self, texts_path, slug, metadata):

        """
        Flush texts.

        Args:
            texts_path (str)
            slug (str)
            metadata (dict)
        """

        text = Text.from_dime_westerns(texts_path, slug, metadata)

        self.corpus.flush(text)


if __name__ == '__main__':
    DimeWesternsExtractor()()
