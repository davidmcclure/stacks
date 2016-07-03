

import os
import pytest
import yaml

from corpus.models import Text
from corpus.utils import read_yaml


pytestmark = pytest.mark.usefixtures('ingest')


cases = read_yaml(__file__, 'ingest.yml')


@pytest.mark.parametrize('identifier,fields', cases.items())
def test_ingest(identifier, fields):
    pass
