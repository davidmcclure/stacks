

from sqlalchemy import Column, Integer, String

from stacks.models import Base
from .text import Text


class EEBOText(Text, Base):

    __tablename__ = 'eebo_text'

    idno_dlps = Column(String, primary_key=True)

    title = Column(String)

    author = Column(String)

    file_extent = Column(String)

    file_pubplace = Column(String)

    file_publisher = Column(String)

    file_date = Column(String)

    # TODO: Take second stc id?
    idno_stc = Column(String)

    idno_eebo_citation = Column(String)

    idno_proquest = Column(String)

    idno_vid = Column(String)

    source_extent = Column(String)

    source_pubplace = Column(String)

    source_publisher = Column(String)

    source_date = Column(Integer)

    language = Column(String)
