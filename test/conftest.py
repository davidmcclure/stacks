

import pytest

import stacks

from stacks import common
from stacks.common.config import Config
from stacks.models import Base


@pytest.fixture(autouse=True)
def test_config():

    """
    Patch in the testing config file.
    """

    common.config = Config.from_test_env()


@pytest.yield_fixture()
def db():

    """
    Reset the testing database, yield a session.
    """

    # Set the test database.
    engine = common.config.build_engine()
    common.session.configure(bind=engine)

    # Reset the tables.
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    yield

    # Clear the session.
    common.session.remove()
