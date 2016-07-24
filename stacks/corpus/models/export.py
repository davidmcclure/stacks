

from sqlalchemy import Column, Integer

from stacks.common.models import Base


class Export(Base):


    __tablename__ = 'export'

    min_year = Column(Integer)

    max_year = Column(Integer)

    sample_size = Column(Integer)
