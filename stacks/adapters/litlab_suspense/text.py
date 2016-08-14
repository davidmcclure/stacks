

from stacks.adapters.litlab import Text as BaseText
from stacks.json_text import JSONText


class Text(BaseText):

    def to_ext_text(self):

        """
        Returns: dict
        """

        return JSONText(dict(
            corpus = 'litlab-suspense',
            identifier = self.identifier(),
            title = self.title(),
            plain_text = self.source_text(),
            author_full = self.author.folder_name(),
            author_first = self.author.name_first(),
            author_last = self.author.name_last(),
            year = self.year(),
        ))
