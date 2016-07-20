

from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

from stacks.common.singletons import session


class Base:

    id = Column(Integer, primary_key=True)

    @classmethod
    def get_by(cls, **kwargs):

        """
        Get the first row that matches a set of filters.
        """

        return cls.query.filter_by(**kwargs).one()


Base = declarative_base(cls=Base)
Base.query = session.query_property()
