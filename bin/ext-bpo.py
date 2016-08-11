#!/usr/bin/env python


from stacks.extractor import Extractor
from stacks.adapters.bpo import Corpus
from stacks.schemas import Text


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

        text = Text.from_bpo(*args, **kwargs)

        self.corpus.flush(text)


if __name__ == '__main__':
    BPOExtractor()()
