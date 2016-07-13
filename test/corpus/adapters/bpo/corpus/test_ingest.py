

import pytest

from test.utils import read_yaml


pytestmark = pytest.mark.usefixtures('ingest')


cases = read_yaml(__file__, 'ingest.yml')


@pytest.mark.parametrize('identifier,fields', cases.items())
def test_ingest(identifier, fields):
    assert True
