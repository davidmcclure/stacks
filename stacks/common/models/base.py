

from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

from stacks.common.utils import commit
from stacks.common.singletons import session


class Base:

    id = Column(Integer, primary_key=True)

    @classmethod
    def create(cls, **kwargs):

        """
        Create and commit a new instance.

        Returns: cls
        """

        row = cls(**kwargs)

        with commit():
            session.add(row)

        return row

    @classmethod
    def get_by(cls, **kwargs):

        """
        Get a row by filters.

        Returns: cls
        """

        return cls.query.filter_by(**kwargs).one()


Base = declarative_base(cls=Base)

Base.query = session.query_property()
