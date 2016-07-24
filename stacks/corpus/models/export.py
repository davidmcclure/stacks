

from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import ARRAY

from stacks.common.models import Base


class Export(Base):


    __tablename__ = 'export'

    # TODO: Use join table?
    corpora = Column(ARRAY(Integer))

    min_year = Column(Integer)

    max_year = Column(Integer)

    sample_size = Column(Integer)
