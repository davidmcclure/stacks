

import attr

from cached_property import cached_property

from stacks.utils import get_text, try_or_log
from stacks.models import ChadhDramaText


@attr.s
class Play:

    xml = attr.ib()

    @cached_property
    def idref(self):
        """Returns: str
        """
        return get_text(self.xml, 'comhd0 idref')

    @try_or_log
    def database(self):
        """Returns: str
        """
        return get_text(self.xml, 'newatts attdbase')

    @try_or_log
    def title(self):
        """Returns: str
        """
        return get_text(self.xml, 'somhead voltitle')

    @try_or_log
    def title_full(self):
        """Returns: str
        """
        return get_text(self.xml, 'source pubtitle')

    @try_or_log
    def author(self):
        """Returns: str
        """
        return get_text(self.xml, 'author nameinv')

    @try_or_log
    def author_id(self):
        """Returns: int
        """
        return int(get_text(self.xml, 'newatts attautid'))

    @try_or_log
    def author_gender(self):
        """Returns: str
        """
        return get_text(self.xml, 'attribs attgend').lower()

    @try_or_log
    def publisher(self):
        """Returns: str
        """
        return get_text(self.xml, 'source citn publ')

    @try_or_log
    def pub_date(self):
        """Returns: int
        """
        return int(get_text(self.xml, 'newatts attpubn1'))

    @try_or_log
    def pub_date2(self):
        """Returns: int
        """
        return int(get_text(self.xml, 'newatts attpubn2'))

    @try_or_log
    def pub_city(self):
        """Returns: str
        """
        return get_text(self.xml, 'source citn city')

    @try_or_log
    def plain_text(self):
        """Returns: str
        """
        # TODO: Scrub out metadata.
        return ' '.join(self.xml.strings)

    def row(self):
        """Assemble a database row.

        Returns: AmficText
        """
        return ChadhDramaText(
            id=self.idref,
            database=self.database(),
            title=self.title(),
            title_full=self.title_full(),
            author=self.author(),
            author_id=self.author_id(),
            author_gender=self.author_gender(),
            publisher=self.publisher(),
            pub_date=self.pub_date(),
            pub_date2=self.pub_date2(),
            pub_city=self.pub_city(),
            text=self.plain_text(),
        )
