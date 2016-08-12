

from stacks.adapters.litlab import Text as BaseText
from stacks.json_text import JSONText


class Text(BaseText):

    def to_json_text(self):

        """
        Returns: dict
        """

        return JSONText(dict(
            corpus = 'litlab-c20',
            identifier = self.identifier(),
            title = self.title(),
            plain_text = self.source_text(),
            author_name_full = self.author.folder_name(),
            author_name_first = self.author.name_first(),
            author_name_last = self.author.name_last(),
            year = self.year(),
        ))
