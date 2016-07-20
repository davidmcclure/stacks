

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


def with_flush(f):

    """
    Flush after a function.

    Returns: func
    """

    @wraps(f)
    def wrapper(*args, **kwargs):

        with rollback():
            res = f(*args, **kwargs)
            session.flush()
            return res

    return wrapper


def with_commit(f):

    """
    Commit after a function.

    Returns: func
    """

    @wraps(f)
    def wrapper(*args, **kwargs):

        with rollback():
            res = f(*args, **kwargs)
            session.commit()
            return res

    return wrapper
