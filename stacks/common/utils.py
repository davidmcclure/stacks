

from functools import wraps

from sqlalchemy.exc import DatabaseError

from .singletons import session


def with_flush(f):

    """
    Flush after a function.

    Returns: func
    """

    @wraps(f)
    def wrapper(*args, **kwargs):

        try:
            res = f(*args, **kwargs)
            session.flush()
            return res

        except DatabaseError:
            session.rollback()
            raise

    return wrapper


def with_commit(f):

    """
    Commit after a function.

    Returns: func
    """

    @wraps(f)
    def wrapper(*args, **kwargs):

        try:
            res = f(*args, **kwargs)
            session.commit()
            return res

        except DatabaseError:
            session.rollback()
            raise

    return wrapper
