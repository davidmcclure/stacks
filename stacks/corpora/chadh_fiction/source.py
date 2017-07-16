

from cached_property import cached_property

from stacks.utils import get_text
from stacks.sources import XMLSource

from .text import Text


class Source(XMLSource):

    def texts(self):
        """Yields: Text
        """
        for tree in self.xml.find_all('div0'):
            yield Text(tree)

    def rows(self):
        """Produce rows for each text.
        """
        for text in self.texts():
            yield text.row()

    @cached_property
    def idref(self):
        """Returns: str
        """
        # Does it work to just take the first idref?
        return get_text(self.xml, 'comhd0 idref')
