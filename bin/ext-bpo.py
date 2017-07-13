#!/usr/bin/env python


from stacks.extractor import Extractor
from stacks.corpora.bpo import Corpus, Article


class BPOExtractor(Extractor):

    def args(self):
        """Provide a list of BPO .zip path / .xml name dicts.

        Returns: list
        """
        corpus = Corpus.from_env()

        return [
            dict(zipfile_path=zpath, xml_name=name)
            for zpath, name in corpus.xml_paths()
        ]

    def flush(self, *args, **kwargs):
        """Flush a text.
        """
        article = Article.from_file(*args, **kwargs)

        self.corpus.index_rows('bpo', article.record_id, article.article_row())


if __name__ == '__main__':
    BPOExtractor()()
