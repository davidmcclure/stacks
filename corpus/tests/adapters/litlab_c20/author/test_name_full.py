

from corpus.adapters.litlab_c20.author import Author


def test_name_full(get_author):

    stephen_king = get_author('King, Stephen')

    assert stephen_king.name_full() == 'King, Stephen'
