

from sqlalchemy import Column, Integer, String, Date

from stacks.models import Base
from .text import Text


class GaleText(Text, Base):

    __tablename__ = 'gale_text'

    psmid = Column(String, primary_key=True)

    asset_id = Column(String)

    asset_id_e_toc = Column(String)

    div_collection_id = Column(String)

    bibliographic_id = Column(String)

    reel = Column(String)

    mcode = Column(String)

    ocr = Column(String)

    pub_date_irregular = Column(String)

    pub_date_composed = Column(String)

    pub_date_start = Column(Integer)

    release_date = Column(Date)

    source_library_name = Column(String)

    source_library_location = Column(String)

    language = Column(String)

    document_type = Column(String)

    notes = Column(String)

    author_composed = Column(String)

    author_first = Column(String)

    author_middle = Column(String)

    author_last = Column(String)

    author_birth_date = Column(Integer)

    author_death_date = Column(Integer)

    full_title = Column(String)

    display_title = Column(String)

    imprint_full = Column(String)

    imprint_publisher = Column(String)

    collation = Column(String)

    publication_place_city = Column(String)

    publication_place_state = Column(String)

    publication_place_country = Column(String)

    publication_place_composed = Column(String)

    total_pages = Column(Integer)
