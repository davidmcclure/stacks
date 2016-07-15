

import pytest

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

    # TODO|dev

    engine = config.build_sqla_engine()

    conn = engine.connect()

    trans = conn.begin_nested()

    session.configure(bind=conn)

    yield

    session.close()

    trans.rollback()

    session.remove()


@pytest.fixture
def rq():

    """
    Clear the RQ queue.
    """

    _rq.connection.flushdb()
