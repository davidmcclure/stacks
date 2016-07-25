

import uuid

from sqlalchemy import Column, Integer, Boolean
from sqlalchemy.dialects.postgresql import ARRAY, UUID

from stacks.common.models import Base


# TODO: Rename to Query?
class Export(Base):


    __tablename__ = 'export'

    # TODO: Make this primary key?
    uuid = Column(UUID)

    # TODO: Use join table?
    corpora = Column(ARRAY(Integer))

    min_year = Column(Integer)

    max_year = Column(Integer)

    sample_size = Column(Integer)

    finished = Column(Boolean, nullable=False, default=False)


    @classmethod
    def create(cls, **kwargs):

        """
        Set the uuid.

        Returns: cls
        """

        return super().create(
            uuid=str(uuid.uuid4()),
            **kwargs
        )
