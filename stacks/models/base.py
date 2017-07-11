

from sqlalchemy.ext.declarative import declarative_base

from stacks import session


class Base:

    @classmethod
    def create(cls, **kwargs):
        """Create a new instance and add it to the session.

        Returns: cls
        """
        row = cls(**kwargs)

        session.add(row)

        return row

    @classmethod
    def get_by(cls, **kwargs):
        """Get a row by filters.

        Returns: cls
        """
        return cls.query.filter_by(**kwargs).one()

    def columns(self):
        """Get a list of column names.

        Returns: list
        """
        return [c.name for c in self.__table__.columns]

    def __iter__(self):
        """Generate column / value tuples.

        Yields: (key, val)
        """
        for key in self.columns():
            yield (key, getattr(self, key))


Base = declarative_base(cls=Base)

Base.query = session.query_property()
