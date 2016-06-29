

import pytest

from stacks import config as _config
from stacks.models import Base


@pytest.fixture(scope='session', autouse=True)
def test_config():

    """
    Register the testing config file.
    """

    _config.paths.append('~/.stacks.test.yml')
    _config.build()


@pytest.yield_fixture
def config():

    """
    Reset the configuration object after each test.

    Yields:
        The modify-able config object.
    """

    yield _config
    _config.build()


@pytest.fixture()
def db(config):

    """
    Create / reset the testing database.
    """

    engine = config.build_engine()

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
