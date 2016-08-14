#!/usr/bin/env python


from stacks.extractor import Extractor
from stacks.adapters.bpo import Corpus, Article
from stacks.ext import corpus


class BPOExtractor(Extractor):

    def args(self):

        """
        Provide a list of BPO .zip path / .xml name dicts.

        Returns: list
        """

        corpus = Corpus.from_env()

        return [
            dict(zipfile_path=zpath, xml_name=name)
            for zpath, name in corpus.xml_paths()
        ]

    def flush(self, *args, **kwargs):

        """
        Flush a text.
        """

        article = Article(*args, **kwargs)

        corpus.insert_text(article.to_json_text())


if __name__ == '__main__':
    BPOExtractor()()
