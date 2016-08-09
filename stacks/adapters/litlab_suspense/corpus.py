

import os

from stacks.utils import scan_paths
from stacks.models import Corpus as StacksCorpus
from stacks.singletons import session

from stacks.adapters.litlab.jobs import ingest


class Corpus:

    def __init__(self, path):

        """
        Canonicalize the corpus path.

        Args:
            path (str)
        """

        self.path = os.path.abspath(path)

    def text_paths(self):

        """
        Generate a path for each text directory.

        Yields: str
        """

        groups = [
            'Suspenseful',
            'Unsuspenseful',
        ]

        # Groups
        for group in groups:

            group_dir = os.path.join(self.path, group)

            # Authors
            for author_dir in next(os.walk(group_dir))[1]:

                author_path = os.path.join(group_dir, author_dir)

                # Texts
                for text_dir in next(os.walk(author_path))[1]:
                    yield os.path.join(author_path, text_dir)

    def ingest(self):

        """
        Queue ingest jobs for each text.
        """

        corpus = StacksCorpus.replace(
            slug='litlab-suspense',
            name='Literary Lab Suspense Corpus',
        )

        session.commit()

        corpus.queue_ingest(ingest, self.text_paths())
