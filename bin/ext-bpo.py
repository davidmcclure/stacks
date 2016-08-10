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

    def flush(self, zipfile_path, xml_name):

        """
        Flush a text.

        Args:
            path (str)
        """

        text = Text.from_bpo(zipfile_path, xml_name)

        self.corpus.flush(text)


if __name__ == '__main__':
    BPOExtractor()()
