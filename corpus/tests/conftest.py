

import pytest
import django_rq


@pytest.yield_fixture(scope='module')
def django_db_module(_django_db_setup, _django_cursor_wrapper):

    """
    Mock the Django database at the module level.
    """

    with _django_cursor_wrapper:
        yield


@pytest.fixture
def redis():

    """
    Clear Redis.
    """

    django_rq.get_connection('default').flushdb()
