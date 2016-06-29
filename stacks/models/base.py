

from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base


class BaseModel:
    id = Column(Integer, primary_key=True)


BaseModel = declarative_base()
