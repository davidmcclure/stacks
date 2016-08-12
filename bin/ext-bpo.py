#!/usr/bin/env python


from stacks.extractor import Extractor
from stacks.adapters.bpo import Corpus, Article


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

        self.corpus.flush(article.as_ext())


if __name__ == '__main__':
    BPOExtractor()()
