

from stacks.utils import tokenize


def test_pos_tag():

    tokens = tokenize('My name is David.')

    assert tokens[0]['token'] == 'my'
    assert tokens[0]['pos'] == 'PRP$'

    assert tokens[1]['token'] == 'name'
    assert tokens[1]['pos'] == 'NN'

    assert tokens[2]['token'] == 'is'
    assert tokens[2]['pos'] == 'VBZ'

    assert tokens[3]['token'] == 'david'
    assert tokens[3]['pos'] == 'NNP'

    assert tokens[4]['token'] == '.'
    assert tokens[4]['pos'] == '.'


def test_char_offsets():

    tokens = tokenize('12 34 56')

    assert tokens[0]['token'] == '12'
    assert tokens[0]['char1'] == 0
    assert tokens[0]['char2'] == 2

    assert tokens[1]['token'] == '34'
    assert tokens[1]['char1'] == 3
    assert tokens[1]['char2'] == 5

    assert tokens[2]['token'] == '56'
    assert tokens[2]['char1'] == 6
    assert tokens[2]['char2'] == 8
