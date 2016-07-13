

import pytest


pytestmark = pytest.mark.usefixtures('ingest')


def test_ingest():
    assert True
