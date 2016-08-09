

from invoke import task

from stacks.singletons import config
from stacks.models import Base

# Register models:
from stacks.models import Text


@task
def init_db(ctx):

    """
    Create database tables.
    """

    engine = config.build_sqla_engine()

    Base.metadata.create_all(engine)
