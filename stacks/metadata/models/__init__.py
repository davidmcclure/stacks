

from stacks import config

from .base import Base
from .text import Text


def reset_db():

    """
    Drop and recreate all tables.
    """

    engine = config.build_sqla_engine()

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
