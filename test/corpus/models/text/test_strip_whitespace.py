

import pytest

from test.corpus.factories import TextFactory


@pytest.mark.parametrize('field', [
    'title',
    'author_name_full',
    'author_name_first',
    'author_name_last',
])
def test_strip_whitespace(field):
    text = TextFactory(**{field: '  value  '})
    assert getattr(text, field) == 'value'
