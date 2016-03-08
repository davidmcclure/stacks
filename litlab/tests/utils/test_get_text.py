

import pytest

from bs4 import BeautifulSoup

from litlab.utils import get_text


@pytest.mark.parametrize('tag,text', [

    ('<tag>Tag Text</tag>', 'Tag Text'),

    # Strip whitespace.
    ('<tag>  Tag Text  </tag>', 'Tag Text'),

    # Empty text -> None.
    ('<tag></tag>', None),
    ('<tag>  </tag>', None),

    # Missing -> None.
    ('', None),

])
def test_get_text(tag, text):
    tree = BeautifulSoup(tag, 'lxml')
    assert get_text(tree, 'tag') == text
