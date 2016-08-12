

from stacks.adapters.litlab import Text as BaseText


class Text(BaseText):

    def as_ext(self):

        """
        Returns: dict
        """

        return dict(
            corpus = 'litlab-c20',
            identifier = self.identifier(),
            title = self.title(),
            plain_text = self.source_text(),
            author_name_full = self.author.folder_name(),
            author_name_first = self.author.name_first(),
            author_name_last = self.author.name_last(),
            year = self.year(),
        )
