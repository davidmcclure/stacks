#!/usr/bin/env python


from stacks.extractor import Extractor
from stacks.corpora.bpo import Corpus, Article


class BPOExtractor(Extractor):

    def args(self):
        """Provide a list of BPO .zip path / .xml name dicts.

        Returns: list
        """
        corpus = Corpus.from_env()

        return list(corpus.article_paths())

    def flush(self, path):
        """Flush a text.
        """
        article = Article.from_file(path)

        self.corpus.index_rows('bpo', article.record_id, *article.rows())


if __name__ == '__main__':
    BPOExtractor()()
