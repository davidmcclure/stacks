#!/usr/bin/env python


from stacks.extractor import Extractor
from stacks.raw.chicago import Corpus, Novel


class ChicagoExtractor(Extractor):

    def args(self):
        """Provide a list of source paths.

        Returns: list
        """
        corpus = Corpus.from_env()

        return [
            dict(corpus_path=corpus.path, metadata=row)
            for row in corpus.novels_metadata()
        ]

    def flush(self, *args, **kwargs):
        """Flush texts.
        """
        novel = Novel(*args, **kwargs)

        self.corpus.insert_text(novel.to_ext_text())


if __name__ == '__main__':
    ChicagoExtractor()()
