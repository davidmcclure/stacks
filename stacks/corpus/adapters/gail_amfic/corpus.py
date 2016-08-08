

import os

from stacks.corpus.utils import scan_paths
from stacks.corpus.models import Corpus as StacksCorpus
from stacks.common.singletons import config, session

from .jobs import ingest


class Corpus:

    @classmethod
    def from_env(cls):

        """
        Wrap the ENV-defined directory.

        Returns: cls
        """

        # TODO: ENV-ify the dir name?
        path = os.path.join(config['data']['raw'], 'gail-amfic')

        return cls(path)

    def __init__(self, path):

        """
        Canonicalize the corpus path.

        Args:
            path (str)
        """

        self.path = os.path.abspath(path)

    def text_paths(self):

        """
        Generate paths to the XML sources.

        Yields: str
        """

        return scan_paths(self.path, '\.xml$')

    def ingest(self):

        """
        Queue ingest jobs for each text.
        """

        corpus = StacksCorpus.replace(
            slug='gail-american-fiction',
            name='Gail American Fiction',
        )

        session.commit()

        corpus.queue_ingest(ingest, self.text_paths())
