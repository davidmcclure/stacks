

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
def flush():

    """
    Flush around a block.
    """

    with rollback():
        yield
        session.flush()


@contextmanager
def commit():

    """
    Flush around a block.
    """

    with rollback():
        yield
        session.commit()


def with_flush(f):

    """
    Flush around a function.

    Returns: func
    """

    @wraps(f)
    def wrapper(*args, **kwargs):
        with flush():
            return f(*args, **kwargs)

    return wrapper


def with_commit(f):

    """
    Commit around a function.

    Returns: func
    """

    @wraps(f)
    def wrapper(*args, **kwargs):
        with commit():
            return f(*args, **kwargs)

    return wrapper
