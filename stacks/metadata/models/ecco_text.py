

from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String,
    UniqueConstraint,
    Text,
    DateTime,
    Date,
)

from stacks.metadata.models import Base


class ECCOText(Base):

    __tablename__ = 'ecco_text'

    document_id = Column(String, primary_key=True)

    estc_id = Column(String)

    unit = Column(Integer)

    reel = Column(Integer)

    mcode = Column(String)

    pub_date = Column(Date)

    release_date = Column(Date)

    source_bib_citation = Column(String)

    source_library = Column(String)

    language = Column(String)

    module = Column(String)

    document_type = Column(String)

    notes = Column(String)

    author_marc_name = Column(String)

    author_death_date = Column(Integer)

    author_marc_date = Column(String)

    full_title = Column(String)

    display_title = Column(String)

    imprint_full = Column(String)

    imprint_city = Column(String)

    imprint_publisher = Column(String)

    imprint_year = Column(String)

    collation = Column(String)

    publication_place = Column(String)

    total_pages = Column(Integer)


class ECCOSubjectHead(Base):

    __tablename__ = 'ecco_subject_head'

    type = Column(String)

    sub_field = Column(String)

    value = Column(String)
