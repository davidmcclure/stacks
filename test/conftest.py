

import pytest

import stacks

from stacks.common import singletons
from stacks.common.config import Config
from stacks.common.models import Base


@pytest.fixture(scope='session', autouse=True)
def set_test_config():

    """
    Patch in the testing config file.
    """

    singletons.config = Config.from_test_env()


@pytest.fixture(scope='session', autouse=True)
def init_testing_db(set_test_config):

    """
    Patch in the testing config file.
    """

    # Apply the testing config.
    engine = singletons.config.build_sqla_engine()
    singletons.session.configure(bind=engine)

    # Reset the tables.
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


@pytest.yield_fixture()
def db():

    """
    Reset the testing database, yield a session.
    """

    yield

    singletons.session.rollback()
    singletons.session.remove()
