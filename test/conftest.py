

import pytest
import os
import tempfile
import shutil

from sqlalchemy import event

from stacks import session, config as _config
from stacks.models import Base
from stacks.corpus import Corpus


@pytest.fixture(scope='session', autouse=True)
def init_testing_db():
    """Drop and recreate the tables.
    """
    engine = _config.build_sqla_engine()

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


@pytest.yield_fixture
def db():
    """Reset the testing database.
    """
    session.begin_nested()

    yield

    session.remove()


# TODO: Provide at both module and function scope?


@pytest.yield_fixture(scope='module')
def config():
    """Clear changes to the config dict.
    """
    # Copy settings.
    old = _config.copy()

    yield _config

    # Restore settings.
    _config.clear()
    _config.update(old)


@pytest.yield_fixture(scope='module')
def temp_dir():
    """Create and clean up a temp directory.
    """
    path = tempfile.mkdtemp()

    yield path

    shutil.rmtree(path)


@pytest.fixture(scope='module')
def raw_fixtures(config):
    """Patch in the `raw` fixtures.
    """
    path = os.path.join(os.path.dirname(__file__), 'fixtures/raw')

    config['data']['raw'] = path


@pytest.fixture(scope='module')
def ext_dir(config, temp_dir):
    """Patch in a temporary `ext` directory.
    """
    config['data']['ext'] = temp_dir


@pytest.yield_fixture(scope='module')
def ext_corpus(ext_dir):
    """Wrap a Corpus instance around the patched `ext` dir.
    """
    yield Corpus.from_env()


@pytest.yield_fixture(scope='module')
def mpi(raw_fixtures, ext_dir, config):
    """Write the config into /tmp/stacks.yml.
    """
    config.lock()

    yield

    config.unlock()

    session.remove()

    init_testing_db()
