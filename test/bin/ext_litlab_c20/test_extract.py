

import pytest

from test.utils import read_yaml


pytestmark = pytest.mark.usefixtures('extract')


cases = read_yaml(__file__, 'texts.yml')


@pytest.mark.parametrize('identifier,fields', cases.items())
def test_extract(identifier, fields, ext_corpus):

    text = ext_corpus.read('litlab-c20', identifier)

    if 'title' in fields:
        assert text['title'] == fields['title']

    if 'author_name_full' in fields:
        assert text['author_name_full'] == fields['author_name_full']

    if 'author_name_first' in fields:
        assert text['author_name_first'] == fields['author_name_first']

    if 'author_name_last' in fields:
        assert text['author_name_last'] == fields['author_name_last']

    if 'year' in fields:
        assert text['year'] == fields['year']

    if 'text' in fields:
        assert fields['text'] in text['plain_text']
