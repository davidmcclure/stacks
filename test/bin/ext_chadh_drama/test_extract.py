

import pytest

from test.utils import read_yaml


pytestmark = pytest.mark.usefixtures('extract')


cases = read_yaml(__file__, 'texts.yml')


@pytest.mark.skip
@pytest.mark.parametrize('identifier,fields', cases.items())
def test_extract(identifier, fields, ext_corpus):

    text = ext_corpus.get_text('chadh-drama', identifier)

    if 'title' in fields:
        assert text.title == fields['title']

    if 'author_full' in fields:
        assert text.author_full == fields['author_full']

    if 'year' in fields:
        assert text.year == fields['year']

    if 'text' in fields:
        assert fields['text'] in text.plain_text
