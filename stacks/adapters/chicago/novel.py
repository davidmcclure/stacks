

import os


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

    def source_text_path(self):

        """
        Returns: str
        """

        return os.path.join(
            self.corpus_path,
            'Texts',
            self.metadata['FILENAME'],
        )

    def source_text(self):

        """
        Returns: str
        """

        with open(
            self.source_text_path(),
            mode='r',
            encoding='utf8',
            errors='ignore'
        ) as fh:

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

    def author_name_first(self):

        """
        Returns: str
        """

        return self.metadata['AUTH_FIRST']

    def author_name_last(self):

        """
        Returns: str
        """

        return self.metadata['AUTH_LAST']

    def author_name_full(self):

        """
        Returns: str
        """

        return '{0}, {1}'.format(
            self.author_name_last(),
            self.author_name_first(),
        )

    def year(self):

        """
        Returns: int
        """

        return int(self.metadata['PUBL_DATE'])

    def as_ext(self):

        """
        Returns: dict
        """

        return dict(
            corpus = 'chicago',
            identifier = self.identifier(),
            title = self.title(),
            plain_text = self.source_text(),
            author_name_full = self.author_name_full(),
            author_name_first = self.author_name_first(),
            author_name_last = self.author_name_last(),
            year = self.year(),
        )
