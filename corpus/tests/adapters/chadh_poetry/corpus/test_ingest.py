

import os
import pytest
import yaml

from corpus.models import Text
from corpus.utils import read_yaml


pytestmark = pytest.mark.usefixtures('ingest')


cases = read_yaml(__file__, 'ingest.yml')


@pytest.mark.chad
@pytest.mark.parametrize('identifier,fields', cases.items())
def test_ingest(identifier, fields):

    text = Text.objects.get(identifier=identifier)

    if 'title' in fields:
        assert text.title == fields['title']

    if 'author_name_full' in fields:
        assert text.author_name_full == fields['author_name_full']

    if 'year' in fields:
        assert text.year == fields['year']

    if 'text' in fields:
        assert fields['text'] in text.plain_text
