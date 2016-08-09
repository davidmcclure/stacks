

import pytest
import os

from sqlalchemy import event

from stacks.singletons import session, config as _config
from stacks.models import Base


@pytest.fixture(scope='session', autouse=True)
def init_testing_db():

    """
    Drop and recreate the tables.
    """

    engine = _config.build_sqla_engine()

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


@pytest.yield_fixture(scope='module')
def db():

    """
    Reset the testing database.
    """

    session.begin_nested()

    yield

    session.remove()


@pytest.yield_fixture(scope='module')
def config():

    """
    Clear changes to the config dict.
    """

    old = _config.config.copy()

    yield _config

    _config.config = old


@pytest.fixture(scope='module')
def raw_fixtures(config):

    """
    Patch in the `raw` fixtures.
    """

    path = os.path.join(os.path.dirname(__file__), 'fixtures/raw')

    config['data']['raw'] = path


@pytest.yield_fixture(scope='module')
def mpi(raw_fixtures, config):

    """
    Write the current configuration into the /tmp/.lint.yml file.
    """

    config.write_tmp()

    yield

    config.clear_tmp()

    session.remove()

    init_testing_db()
