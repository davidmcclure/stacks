

from contextlib import contextmanager
from functools import wraps

from sqlalchemy.exc import DatabaseError

from .singletons import session


@contextmanager
def rollback():

    """
    Catch DatabaseError, rollback.
    """

    try: yield

    except DatabaseError:
        session.rollback()
        raise


@contextmanager
def commit():

    """
    Flush around a block.
    """

    with rollback():
        yield
        session.commit()
