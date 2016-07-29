

import uuid

from sqlalchemy import Column, Integer, Boolean
from sqlalchemy.dialects.postgresql import ARRAY

from stacks.common.models import Base


class Export(Base):


    __tablename__ = 'export'

    # TODO: Use join table?
    corpora = Column(ARRAY(Integer))

    min_year = Column(Integer)

    max_year = Column(Integer)

    finished = Column(Boolean, nullable=False, default=False)
