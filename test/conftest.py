

import pytest

from sqlalchemy import event

from stacks.common.singletons import config, session, rq as _rq
from stacks.common.models import Base


@pytest.fixture(scope='session', autouse=True)
def init_testing_db():

    """
    Patch in the testing config file.
    """

    # Apply the testing config.
    engine = config.build_sqla_engine()
    session.configure(bind=engine)

    # Reset the tables.
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


@pytest.yield_fixture()
def db():

    """
    Reset the testing database.
    """

    session.begin_nested()

    yield

    session.remove()


# TODO: dry
@pytest.yield_fixture(scope='module')
def db_module():

    """
    Reset the testing database.
    """

    session.begin_nested()

    yield

    session.remove()


@pytest.fixture
def rq():

    """
    Clear the RQ queue.
    """

    _rq.connection.flushdb()


# TODO: dry
@pytest.fixture(scope='module')
def rq_module():

    """
    Clear the RQ queue.
    """

    _rq.connection.flushdb()
