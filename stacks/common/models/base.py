

from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

from stacks.common.singletons import session


class Base:

    id = Column(Integer, primary_key=True)

    @classmethod
    def create(cls, **kwargs):

        """
        Create a new instance and add it to the session.

        Returns: cls
        """

        row = cls(**kwargs)

        session.add(row)

        return row

    @classmethod
    def get_by(cls, **kwargs):

        """
        Get a row by filters.

        Returns: cls
        """

        return cls.query.filter_by(**kwargs).one()

    def columns(self):

        """
        Get a list of column names.

        Returns: list
        """

        return [c.name for c in self.__table__.columns]

    def asdict(self):

        """
        Cast the instance to a dict.

        Returns: dict
        """

        return dict([(c, getattr(self, c)) for c in self.columns()])


Base = declarative_base(cls=Base)

Base.query = session.query_property()
