

import os

from slugify import slugify

from stacks.utils import scan_paths
from stacks.json_text import JSONText


class Text:

    def __init__(self, texts_path, metadata):

        """
        Canonicalize the texts path, set the text metadata.

        Args:
            texts_path (str)
            metadata (dict)
        """

        self.texts_path = os.path.abspath(texts_path)

        self.metadata = metadata

    def source_text_path(self):

        """
        Returns: str
        """

        paths = list(scan_paths(self.texts_path, '\.txt$'))

        for path in paths:

            fname = os.path.basename(path)

            # Find path that starts with the title.
            if fname.startswith(self.title()):
                return path

    def source_text(self):

        """
        Returns: str
        """

        with open(
            self.source_text_path(),
            mode='r',
            encoding='utf8',
            errors='ignore',
        ) as fh:

            return fh.read()

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

        return int(self.metadata['ORIG_PUBL_DATE'])

    def identifier(self):

        """
        Make a slug from the surname + title.

        Returns: str
        """

        return slugify(' '.join([
            self.author_name_last(),
            self.title(),
        ]))

    def to_json_text(self):

        """
        Returns: dict
        """

        return JSONText(dict(
            corpus = 'price-lab',
            identifier = self.identifier(),
            title = self.title(),
            plain_text = self.source_text(),
            author_name_full = self.author_name_full(),
            author_name_first = self.author_name_first(),
            author_name_last = self.author_name_last(),
            year = self.year(),
        ))
