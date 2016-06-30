

import pytest

from stacks.common import config as _config, session
from stacks.models import Base


@pytest.fixture(scope='session', autouse=True)
def test_config():

    """
    Register the testing config file.
    """

    _config.paths.append('~/.stacks.test.yml')
    _config.read()


@pytest.yield_fixture
def config():

    """
    Reset the configuration object after each test.

    Yields:
        The modify-able config object.
    """

    yield _config
    _config.read()


@pytest.yield_fixture()
def db(config):

    """
    Reset the testing database, yield a session.
    """

    engine = config.build_engine()

    session.configure(bind=engine)

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    yield

    session.remove()
