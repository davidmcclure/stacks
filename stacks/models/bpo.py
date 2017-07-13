

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

    publisher = Column(String)

    alpha_pub_date = Column(String)

    numeric_pub_date = Column(Date)

    source_type = Column(String)

    object_type = Column(String)

    language_code = Column(String)

    issn = Column(String)

    start_page = Column(Integer)

    end_page = Column(Integer)

    pagination = Column(String)

    url_doc_view = Column(String)

    abstract = Column(String)


class BPOContributor(Base):

    __tablename__ = 'bpo_contributor'

    id = Column(Integer, primary_key=True)

    record_id = Column(String, nullable=False)

    role = Column(String)

    last_name = Column(String)

    middle_name = Column(String)

    first_name = Column(String)

    person_name = Column(String)

    original_form = Column(String)


class BPOFlexTerm(Base):

    __tablename__ = 'bpo_flex_term'

    id = Column(Integer, primary_key=True)

    record_id = Column(String, nullable=False)

    name = Column(String)

    value = Column(String)
