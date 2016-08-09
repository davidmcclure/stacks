

import pytest


pytestmark = pytest.mark.usefixtures('extract')


def test_extract():
    assert True
