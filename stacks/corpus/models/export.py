

from sqlalchemy import Column, Integer, Boolean
from sqlalchemy.dialects.postgresql import ARRAY, UUID

from stacks.common.models import Base


class Export(Base):


    __tablename__ = 'export'

    uuid = Column(UUID)

    # TODO: Use join table?
    corpora = Column(ARRAY(Integer))

    min_year = Column(Integer)

    max_year = Column(Integer)

    sample_size = Column(Integer)

    finished = Column(Boolean, nullable=False)
