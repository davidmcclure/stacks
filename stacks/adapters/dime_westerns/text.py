

import os


class Text:

    def __init__(self, texts_path, slug, metadata):

        """
        Set the texts path, slug, and metadata.

        Args:
            texts_path (str)
            slug (str)
            metadata (dict)
        """

        self.texts_path = os.path.abspath(texts_path)

        self.slug = slug

        self.metadata = metadata

    def source_text_path(self):

        """
        Returns: str
        """

        fname = '{0}.txt'.format(self.identifier())

        return os.path.join(self.texts_path, fname);

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

        return self.metadata['Title']

    def author_name_full(self):

        """
        Returns: str
        """

        return self.metadata['Author']

    def year(self):

        """
        Returns: int
        """

        return int(self.metadata['Year'])

    def identifier(self):

        """
        Make a slug from the slug + year.

        Returns: str
        """

        return self.slug + str(self.year())
