

from invoke import task

from stacks.common.singletons import config
from stacks.common.models import Base


@task
def init_db(ctx):

    """
    Create database tables.
    """

    engine = config.build_sqla_engine()

    Base.metadata.create_all(engine)
