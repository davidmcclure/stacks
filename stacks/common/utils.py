

from functools import wraps

from sqlalchemy.exc import DatabaseError

from .singletons import session


def with_commit(f):

    """
    Commit after a function.

    Returns: func
    """

    @wraps(f)
    def wrapper(*args, **kwargs):

        try:
            f(*args, **kwargs)
            session.commit()

        except DatabaseError:
            session.rollback()
            raise

    return wrapper
