

from sqlalchemy import Column, Integer, String, Date, Float

from stacks.models import Base
from .text import Text


class NCCOText(Text, Base):

    __tablename__ = 'ncco_text'

    psmid = Column(String, primary_key=True)

    asset_id = Column(String)

    asset_id_e_toc = Column(String)

    dvi_collection_id = Column(String)

    bibliographic_id = Column(String)

    reel = Column(String)

    mcode = Column(String)

    ocr = Column(Float)

    pub_date_start = Column(Integer)

    pub_date_end = Column(Integer)

    release_date = Column(Date)

    source_library_name = Column(String)

    source_library_location = Column(String)

    language = Column(String)

    document_type = Column(String)

    notes = Column(String)

    comments = Column(String)

    author_composed = Column(String)

    author_first = Column(String)

    author_middle = Column(String)

    author_last = Column(String)

    author_birth_date = Column(Integer)

    author_death_date = Column(Integer)

    full_title = Column(String)

    display_title = Column(String)

    volume = Column(Integer)

    total_volumes = Column(Integer)

    imprint_full = Column(String)

    imprint_publisher = Column(String)

    collation = Column(String)

    publication_place_city = Column(String)

    publication_place_state = Column(String)

    publication_place_country = Column(String)

    publication_place_composed = Column(String)

    total_pages = Column(Integer)


class NCCOSubjectHead(Base):

    __tablename__ = 'ncco_subject_head'

    id = Column(Integer, primary_key=True)

    document_id = Column(String)

    type = Column(String)

    sub_field = Column(String)

    value = Column(String)
