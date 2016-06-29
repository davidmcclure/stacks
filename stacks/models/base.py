

from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base


class Base:
    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)
