

import attr

from cached_property import cached_property

from stacks.utils import get_text, try_or_log
from stacks.models import ChadhPoetryText


@attr.s
class Poem:

    xml = attr.ib()

    @cached_property
    def idref(self):
        """Returns: str
        """
        return get_text(self.xml, 'idref')

    @try_or_log
    def attidref(self):
        """Returns: str
        """
        return get_text(self.xml, 'newatts attidref')

    @try_or_log
    def database(self):
        """Returns: str
        """
        return get_text(self.xml, 'newatts attdbase')

    @try_or_log
    def vol_title(self):
        """Returns: str
        """
        return get_text(self.xml, 'newatts atttitle volhead')

    @try_or_log
    def vol_publisher(self):
        """Returns: str
        """
        return get_text(self.xml, 'comcitn pbl')

    @try_or_log
    def vol_date(self):
        """Returns: int
        """
        return int(get_text(self.xml, 'comcitn y1'))

    @try_or_log
    def title(self):
        """Returns: str
        """
        return get_text(self.xml, 'newatts atttitle mainhead')

    @try_or_log
    def author(self):
        """Returns: str
        """
        return get_text(self.xml, 'attribs attpoet')

    @try_or_log
    def author_id(self):
        """Returns: int
        """
        return int(get_text(self.xml, 'newatts attautid'))

    @try_or_log
    def rhyme(self):
        """Returns: bool
        """
        return get_text(self.xml, 'attribs attrhyme') == 'y'

    @try_or_log
    def period(self):
        """Returns: str
        """
        return get_text(self.xml, 'newatts attperi')

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
    def plain_text(self):
        """Returns: str
        """
        # TODO: Does this get everything?
        return ' '.join([
            p.get_text(separator=' ', strip=True).replace('\n', ' ')
            for p in self.xml.find_all('l')
        ])

    def row(self):
        """Assemble a database row.

        Returns: ChadhPoetryText
        """
        return ChadhPoetryText(
            id=self.idref,
            attidref=self.attidref(),
            database=self.database(),
            vol_title=self.vol_title(),
            vol_publisher=self.vol_publisher(),
            vol_date=self.vol_date(),
            title=self.title(),
            author=self.author(),
            author_id=self.author_id(),
            rhyme=self.rhyme(),
            period=self.period(),
            pub_date=self.pub_date(),
            pub_date2=self.pub_date2(),
            text=self.plain_text(),
        )
