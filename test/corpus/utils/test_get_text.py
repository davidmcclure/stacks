

import pytest

from bs4 import BeautifulSoup

from stacks.corpus.utils import get_text


@pytest.mark.parametrize('tag,text', [

    # Unchanged.
    ('<tag>Book Title</tag>', 'Book Title'),

    # Strip whitespace.
    ('<tag>  Book Title  </tag>', 'Book Title'),

    # Empty content -> None.
    ('<tag></tag>', None),
    ('<tag>  </tag>', None),

    # Missing -> None.
    ('', None),

    # Join adjacent texts with a space.
    (
        '''
        <tag>
            <span>text1</span><span>text2</span>
        </tag>
        ''',
        'text1 text2'
    ),

    # Replace \n with space.
    (
        '''
        <tag>
            <span>text1</span>
            <span>text2</span>
        </tag>
        ''',
        'text1 text2'
    ),

])
def test_get_text(tag, text):
    tree = BeautifulSoup(tag, 'lxml')
    assert get_text(tree, 'tag') == text
