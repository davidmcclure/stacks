

import attr

from cached_property import cached_property

from stacks.utils import get_text, try_or_log
from stacks.models import ChadhFictionText


@attr.s
class Text:

    xml = attr.ib()

    @cached_property
    def idref(self):
        """Returns: str
        """
        return get_text(self.xml, 'comhd0 idref')

    @try_or_log
    def attidref(self):
        """Returns: str
        """
        return get_text(self.xml, 'newatts attidref')

    @try_or_log
    def eafidref(self):
        """Returns: str
        """
        return get_text(self.xml, 'newatts eafidref')

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
        return get_text(self.xml, 'attribs attgend')

    @try_or_log
    def period_code(self):
        """Returns: str
        """
        return get_text(self.xml, 'attribs attperi')

    @try_or_log
    def period(self):
        """Returns: str
        """
        return get_text(self.xml, 'newatts attperi')

    # TODO: Handle multiple <attgenre>.
    @try_or_log
    def genre(self):
        """Returns: str
        """
        return get_text(self.xml, 'newatts attgenre')

    @try_or_log
    def database(self):
        """Returns: str
        """
        return get_text(self.xml, 'newatts attdbase')

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
        # TODO: Does this get everything?
        return ' '.join([
            p.get_text(separator=' ', strip=True).replace('\n', ' ')
            for p in self.xml.find_all(['p', 'l'])
        ])

    def row(self):
        """Assemble a database row.

        Returns: AmficText
        """
        return ChadhFictionText(
            id=self.idref,
            attidref=self.attidref(),
            eafidref=self.eafidref(),
            title=self.title(),
            title_full=self.title_full(),
            author=self.author(),
            author_id=self.author_id(),
            author_gender=self.author_gender(),
            period_code=self.period_code(),
            period=self.period(),
            genre=self.genre(),
            database=self.database(),
            publisher=self.publisher(),
            pub_date=self.pub_date(),
            pub_date2=self.pub_date2(),
            pub_city=self.pub_city(),
            text=self.plain_text(),
        )
