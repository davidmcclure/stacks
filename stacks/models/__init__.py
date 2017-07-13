
# flake8: noqa

from stacks import config

from .base import Base
from .ecco import ECCOText, ECCOSubjectHead
from .ncco import NCCOText, NCCOSubjectHead
from .amfic import AmficText
from .bpo import BPOArticle


def reset_db():

    """
    Drop and recreate all tables.
    """

    engine = config.build_sqla_engine()

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
