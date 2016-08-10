

import os
import json
import bz2

from stacks.singletons import config
from stacks.schemas import Text
from stacks.utils import checksum

from stacks.adapters.gail_amfic import Text as GailAmficText
from stacks.adapters.ecco import Text as ECCOText


class ExtCorpus:

    @classmethod
    def from_env(cls):

        """
        Wrap the ENV-defined root.

        Returns: cls
        """

        return cls(config['data']['ext'])

    def __init__(self, path):

        """
        Canonicalize the root path.

        Args:
            path (str)
        """

        self.path = os.path.abspath(path)

    def ext_path(self, corpus, identifier):

        """
        Form the archive path for a text.

        Args:
            corpus (str)
            identifier (str)

        Returns: str
        """

        name = checksum(identifier)

        prefix = name[:3]
        suffix = name[3:]

        # Form the segment path.
        segment = os.path.join(self.path, corpus, prefix)

        # Join on the file name.
        return os.path.join(segment, suffix+'.json.bz2')

    def flush(self, text):

        """
        Flush a text to disk.

        Args:
            text (stacks.schemas.Text)
        """

        text.validate()

        # Form the text path.
        path = self.ext_path(text.corpus, text.identifier)

        # Ensure the directory exists.
        os.makedirs(os.path.dirname(path), exist_ok=True)

        with bz2.open(path, 'wt') as fh:
            json.dump(text.to_primitive(), fh)

    def read(self, corpus, identifier):

        """
        Read JSON from the corpus.

        Args:
            corpus (str)
            identifier (str)

        Returns: dict
        """

        path = self.ext_path(corpus, identifier)

        with bz2.open(path, 'rt') as fh:
            return json.load(fh)

    def flush_gail_amfic(self, path):

        """
        Flush a Gail American Fiction text.

        Args:
            path (str)
        """

        text = GailAmficText(path)

        self.flush(Text(dict(

            corpus = 'gail-amfic',
            identifier = text.identifier(),
            title = text.title(),
            plain_text = text.plain_text(),

            author_name_full = text.author_name_full(),
            author_name_first = text.author_name_first(),
            author_name_last = text.author_name_last(),

            year = text.year(),

        )))

    def flush_ecco(self, path):

        """
        Flush an ECCO text.

        Args:
            path (str)
        """

        text = ECCOText(path)

        self.flush(Text(dict(

            corpus = 'ecco',
            identifier = text.identifier(),
            title = text.title(),
            plain_text = text.plain_text(),

            author_name_full = text.author_marc_name(),

            year = text.year(),

        )))
