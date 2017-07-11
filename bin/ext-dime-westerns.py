#!/usr/bin/env python


from stacks.extractor import Extractor
from stacks.corpora.dime_westerns import Corpus, Text


class DimeWesternsExtractor(Extractor):

    def args(self):
        """Provide a list of source paths.

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
        """Flush texts.
        """
        text = Text(*args, **kwargs)

        self.corpus.insert_text(text.to_ext_text())


if __name__ == '__main__':
    DimeWesternsExtractor()()
