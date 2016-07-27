

import os
import pytest


@pytest.fixture(scope='module')
def fixtures_path():

    """
    Get a corpus fixtures path by slug
    """

    def f(slug):
        return os.path.join(os.path.dirname(__file__), 'fixtures', slug)

    return f
