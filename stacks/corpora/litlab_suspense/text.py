

from stacks.corpora.litlab import Text as BaseText
from stacks.ext import Text as ExtText


class Text(BaseText):

    def to_ext_text(self):
        """Returns: dict
        """
        return ExtText(dict(
            corpus = 'litlab-suspense',
            identifier = self.identifier(),
            title = self.title(),
            plain_text = self.source_text(),
            author_full = self.author.folder_name(),
            author_first = self.author.name_first(),
            author_last = self.author.name_last(),
            year = self.year(),
        ))
