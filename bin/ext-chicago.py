#!/usr/bin/env python


from stacks.extractor import Extractor
from stacks.adapters.chicago import Corpus
from stacks.schemas import Text


class ChicagoExtractor(Extractor):

    def args(self):

        """
        Provide a list of source paths.

        Returns: list
        """

        corpus = Corpus.from_env()

        return [
            dict(corpus_path=corpus.path, metadata=row)
            for row in corpus.novels_metadata()
        ]

    def flush(self, *args, **kwargs):

        """
        Flush texts.

        Args:
            corpus_path (str)
            metadata (dict)
        """

        text = Text.from_chicago(*args, **kwargs)

        self.corpus.flush(text)


if __name__ == '__main__':
    ChicagoExtractor()()
