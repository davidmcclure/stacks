

import os
import json

from schema import Schema, Optional

from stacks.singletons import config
from stacks.text_schema import schema
from stacks.utils import checksum

from stacks.adapters.gail_amfic import Text as GailAmficText


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

    def flush(self, corpus, data):

        """
        Flush a text to disk.

        Args:
            corpus (str)
            data (dict)
        """

        data = schema(data)

        name = checksum(data['identifier'])

        prefix = name[:3]
        suffix = name[3:]

        # Form the segment path.
        segment = os.path.join(self.path, corpus, prefix)

        # Ensure the directory exists.
        os.makedirs(segment, exist_ok=True)

        # Form the text path.
        path = os.path.join(segment, suffix+'.json')

        with open(path, 'w') as fh:
            json.dump(data, fh, indent=2)

    def flush_gail_amfic(self, path):

        """
        Flush a Gail American Fiction text.

        Args:
            path (str)
        """

        text = GailAmficText(path)

        self.flush('gail-amfic', {

            'identifier': text.identifier(),
            'title': text.title(),
            'plain_text': text.plain_text(),

            'author': {
                'name': {
                    'full': text.author_name_full(),
                    'first': text.author_name_first(),
                    'last': text.author_name_last(),
                }
            },

            'year': text.year(),

        })
