

from sqlalchemy import Column, Integer, String

from stacks.models import Base
from .text import Text


class ChadhFictionText(Text, Base):

    __tablename__ = 'chadh_fiction_text'

    id = Column(String, primary_key=True)

    attidref = Column(String)

    eafidref = Column(String)

    title_long = Column(String)

    author = Column(String)

    author_id = Column(Integer)

    author_gender = Column(String)

    period = Column(String)

    genre = Column(String)

    database = Column(String)

    publisher = Column(String)

    pub_date = Column(Integer)

    pub_date2 = Column(Integer)

    pub_city = Column(String)
