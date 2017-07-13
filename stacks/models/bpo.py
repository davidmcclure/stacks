

from sqlalchemy import Column, Integer, String, Date, DateTime

from stacks.models import Base
from .text import Text


class BPOArticle(Text, Base):

    __tablename__ = 'bpo_article'

    record_id = Column(String, primary_key=True)

    date_time_stamp = Column(DateTime)

    action_code = Column(String)

    record_title = Column(String)

    publication_id = Column(Integer)

    publication_title = Column(String)

    publication_qualifier = Column(String)

    source_type = Column(String)

    object_type = Column(String)

    # TODO: contributors

    language_code = Column(String)

    issn = Column(String)

    start_page = Column(Integer)

    end_page = Column(Integer)

    pagination = Column(String)

    url_doc_view = Column(String)

    # TODO: flex terms

    abstract = Column(String)
