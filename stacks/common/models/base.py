

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

        return (
            session
            .query(cls)
            .filter_by(**kwargs)
            .first()
        )


Base = declarative_base(cls=Base)
