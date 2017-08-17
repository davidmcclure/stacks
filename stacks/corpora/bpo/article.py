

import attr

from datetime import datetime as dt
from cached_property import cached_property
from zipfile import ZipFile
from bs4 import BeautifulSoup

from stacks.utils import get_text, try_or_log, parse_8d_date
from stacks.models import BPOArticle, BPOFlexTerm, BPOContributor


@attr.s
class Article:

    xml = attr.ib()

    @classmethod
    def from_file(cls, path):
        """Hydrate from a file path.

        Args:
            path (str)

        Returns: cls
        """
        with open(path, 'r') as fh:
            return cls(BeautifulSoup(fh, 'xml'))

    @cached_property
    def record_id(self):
        """Returns: str
        """
        return get_text(self.xml, 'RecordID')

    @try_or_log
    def date_time_stamp(self):
        """Returns: datetime
        """
        text = get_text(self.xml, 'DateTimeStamp')

        return dt.strptime(text, '%Y%m%d%H%M%S')

    @try_or_log
    def action_code(self):
        """Returns: str
        """
        return get_text(self.xml, 'ActionCode')

    @try_or_log
    def record_title(self):
        """Returns: str
        """
        return get_text(self.xml, 'RecordTitle')

    @try_or_log
    def publication_id(self):
        """Returns: int
        """
        return int(get_text(self.xml, 'PublicationID'))

    @try_or_log
    def publication_title(self):
        """Returns: str
        """
        return get_text(self.xml, 'Publication Title')

    @try_or_log
    def publication_qualifier(self):
        """Returns: str
        """
        return get_text(self.xml, 'Publication Qualifier')

    @try_or_log
    def publisher(self):
        """Returns: str
        """
        return get_text(self.xml, 'Publisher')

    @try_or_log
    def alpha_pub_date(self):
        """Returns: str
        """
        return get_text(self.xml, 'AlphaPubDate')

    @try_or_log
    def numeric_pub_date(self):
        """Returns: date
        """
        return parse_8d_date(get_text(self.xml, 'NumericPubDate'))

    @try_or_log
    def source_type(self):
        """Returns: str
        """
        return get_text(self.xml, 'SourceType')

    @try_or_log
    def object_type(self):
        """Returns: str
        """
        return get_text(self.xml, 'ObjectType')

    @try_or_log
    def language_code(self):
        """Returns: str
        """
        return get_text(self.xml, 'LanguageCode')

    @try_or_log
    def issn(self):
        """Returns: str
        """
        return get_text(self.xml, 'ISSN')

    @try_or_log
    def start_page(self):
        """Returns: int
        """
        return int(get_text(self.xml, 'StartPage'))

    @try_or_log
    def end_page(self):
        """Returns: int
        """
        return int(get_text(self.xml, 'EndPage'))

    @try_or_log
    def pagination(self):
        """Returns: str
        """
        return str(get_text(self.xml, 'Pagination'))

    @try_or_log
    def url_doc_view(self):
        """Returns: str
        """
        return get_text(self.xml, 'URLDocView')

    @try_or_log
    def abstract(self):
        """Returns: str
        """
        xml = get_text(self.xml, 'Abstract')

        return BeautifulSoup(xml, 'xml').text

    @try_or_log
    def full_text(self):
        """Returns: str
        """
        return get_text(self.xml, 'FullText')

    def article_row(self):
        """Build an article row instance.

        Returns: BPOArticle
        """
        return BPOArticle(
            record_id=self.record_id,
            date_time_stamp=self.date_time_stamp(),
            action_code=self.action_code(),
            record_title=self.record_title(),
            publication_id=self.publication_id(),
            publication_title=self.publication_title(),
            publication_qualifier=self.publication_qualifier(),
            publisher=self.publisher(),
            alpha_pub_date=self.alpha_pub_date(),
            numeric_pub_date=self.numeric_pub_date(),
            source_type=self.source_type(),
            object_type=self.object_type(),
            language_code=self.language_code(),
            issn=self.issn(),
            start_page=self.start_page(),
            end_page=self.end_page(),
            pagination=self.pagination(),
            url_doc_view=self.url_doc_view(),
            abstract=self.abstract(),
            text=self.full_text(),
        )

    def flex_term_rows(self):
        """Build a list of flex term rows.

        Returns: list of BPOFlexTerm
        """
        for term in self.xml.select('FlexTerm'):

            yield BPOFlexTerm(
                record_id=self.record_id,
                name=get_text(term, 'FlexTermName'),
                value=get_text(term, 'FlexTermValue'),
            )

    def contributor_rows(self):
        """Build a list of contributor rows.

        Returns: list of BPOContributor
        """
        for contrib in self.xml.select('Contributor'):

            yield BPOContributor(
                record_id=self.record_id,
                role=get_text(contrib, 'ContribRole'),
                last_name=get_text(contrib, 'LastName'),
                middle_name=get_text(contrib, 'MiddleName'),
                first_name=get_text(contrib, 'FirstName'),
                person_name=get_text(contrib, 'PersonName'),
                original_form=get_text(contrib, 'OriginalForm'),
            )

    def rows(self):
        """Assemble list of all database rows.
        """
        return (
            [self.article_row()] +
            list(self.contributor_rows()) +
            list(self.flex_term_rows())
        )
