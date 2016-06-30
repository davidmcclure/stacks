

import pytest

import stacks

from stacks import core
from stacks.core.config import Config
from stacks.core.models import Base


@pytest.fixture(scope='session', autouse=True)
def set_test_config():

    """
    Patch in the testing config file.
    """

    core.config = Config.from_test_env()


@pytest.fixture(scope='session', autouse=True)
def init_testing_db(set_test_config):

    """
    Patch in the testing config file.
    """

    # Apply the testing config.
    engine = core.config.build_engine()
    core.session.configure(bind=engine)

    # Reset the tables.
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


@pytest.yield_fixture()
def db():

    """
    Reset the testing database, yield a session.
    """

    yield

    core.session.rollback()
    core.session.remove()
