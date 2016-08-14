

import pytest

from test.utils import read_yaml


pytestmark = pytest.mark.usefixtures('extract')


cases = read_yaml(__file__, 'texts.yml')


@pytest.mark.parametrize('identifier,fields', cases.items())
def test_extract(identifier, fields, ext_corpus):

    text = ext_corpus.get_text('litlab-c20', identifier)

    if 'title' in fields:
        assert text.title == fields['title']

    if 'author_full' in fields:
        assert text.author_full == fields['author_full']

    if 'author_first' in fields:
        assert text.author_first == fields['author_first']

    if 'author_last' in fields:
        assert text.author_last == fields['author_last']

    if 'year' in fields:
        assert text.year == fields['year']

    if 'text' in fields:
        assert fields['text'] in text.plain_text
