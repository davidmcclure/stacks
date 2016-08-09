

import os

from slugify import slugify

from stacks.utils import scan_paths


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
