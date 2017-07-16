

from sqlalchemy import Column, Integer, String

from stacks.models import Base
from .text import Text


class ChadhFictionText(Text, Base):

    __tablename__ = 'chadh_fiction_text'

    id = Column(String, primary_key=True)

    attidref = Column(String)

    eafidref = Column(String)

    title = Column(String)

    title_full = Column(String)

    author = Column(String)

    author_id = Column(Integer)

    author_gender = Column(String)

    period_code = Column(String)

    genre = Column(String)

    database = Column(String)

    publisher = Column(String)

    pub_date = Column(Integer)

    pub_date2 = Column(Integer)

    pub_city = Column(String)
