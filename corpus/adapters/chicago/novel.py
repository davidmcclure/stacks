

import os

from django.conf import settings


class Novel:

    def __init__(self, corpus_path, metadata):

        """
        Canonicalize the corpus path, set the novel metadata.

        Args:
            corpus_path (str)
            metadata (dict)
        """

        self.corpus_path = os.path.abspath(corpus_path)

        self.metadata = metadata

    def plain_text_path(self):

        """
        Returns: str
        """

        return os.path.join(
            self.corpus_path,
            'Texts',
            self.metadata['FILENAME'],
        )

    def plain_text(self):

        """
        Returns: str
        """

        with open(self.plain_text_path(), 'r') as fh:
            return fh.read()

    def identifier(self):

        """
        Returns: str
        """

        return self.metadata['BOOK_ID']

    def title(self):

        """
        Returns: str
        """

        return self.metadata['TITLE']

    def author(self):

        """
        Returns: str
        """

        return '{0}, {1}'.format(
            self.metadata['AUTH_LAST'],
            self.metadata['AUTH_FIRST'],
        )

    def year(self):

        """
        Returns: int
        """

        return int(self.metadata['PUBL_DATE'])
