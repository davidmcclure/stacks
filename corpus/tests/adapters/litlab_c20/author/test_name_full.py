

import pytest

from corpus.adapters.litlab_c20.author import Author


@pytest.mark.parametrize('author_dir,name_full', [

    ('King, Stephen', 'King, Stephen'),

    ('Kotzwinkle, William', 'Kotzwinkle, William'),

    ('Tolkien, J.R.R.', 'Tolkien, J.R.R.'),

])
def test_name_full(author_dir, name_full, get_author):

    author = get_author(author_dir)

    assert author.name_full() == name_full
