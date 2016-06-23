

import pytest

from corpus.adapters.litlab_c20.author import Author


@pytest.fixture
def stephen_king(get_author):
    return get_author('King, Stephen')


def test_name_full(stephen_king):
    assert stephen_king.name_full() == 'King, Stephen'
