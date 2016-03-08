

import pytest

from bs4 import BeautifulSoup

from litlab.utils import get_text


@pytest.mark.parametrize('tag,text', [

    ('<tag>Book Title</tag>', 'Book Title'),

    # Strip whitespace.
    ('<tag>  Book Title  </tag>', 'Book Title'),

    # Empty text -> None.
    ('<tag></tag>', None),
    ('<tag>  </tag>', None),

    # Missing tag -> None.
    ('', None),

])
def test_get_text(tag, text):
    tree = BeautifulSoup(tag, 'lxml')
    assert get_text(tree, 'tag') == text
