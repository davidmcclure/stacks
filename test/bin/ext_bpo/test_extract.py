

import pytest

from test.utils import read_yaml


pytestmark = pytest.mark.usefixtures('extract')


cases = read_yaml(__file__, 'texts.yml')


@pytest.mark.parametrize('identifier,fields', cases.items())
def test_extract(identifier, fields, json_corpus):

    text = json_corpus.get_text('bpo', identifier)

    if 'title' in fields:
        assert text.metadata.title == fields['title']

    if 'author_name_full' in fields:
        assert text.metadata.author.name.full == fields['author_name_full']

    if 'author_name_first' in fields:
        assert text.metadata.author.name.first == fields['author_name_first']

    if 'author_name_last' in fields:
        assert text.metadata.author.name.last == fields['author_name_last']

    if 'year' in fields:
        assert text.metadata.year == fields['year']

    if 'text' in fields:
        assert fields['text'] in text.text
