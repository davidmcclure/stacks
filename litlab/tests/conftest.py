

import pytest
import django_rq


@pytest.fixture
def redis():

    """
    Clear Redis.
    """

    django_rq.get_connection('default').flushdb()
