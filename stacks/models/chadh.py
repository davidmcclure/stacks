

from sqlalchemy import Column, Integer, String, Boolean

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

    period = Column(String)

    genre = Column(String)

    database = Column(String)

    publisher = Column(String)

    pub_date = Column(Integer)

    pub_date2 = Column(Integer)

    pub_city = Column(String)


class ChadhPoetryText(Text, Base):

    __tablename__ = 'chadh_poetry_text'

    id = Column(String, primary_key=True)

    attidref = Column(String)

    database = Column(String)

    vol_title = Column(String)

    vol_publisher = Column(String)

    vol_date = Column(Integer)

    title = Column(String)

    author = Column(String)

    author_id = Column(Integer)

    rhyme = Column(Boolean)

    period = Column(String)

    pub_date = Column(Integer)

    pub_date2 = Column(Integer)
