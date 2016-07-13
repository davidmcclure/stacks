

import pytest

from stacks.corpus.utils import slug_is_valid


@pytest.mark.parametrize('slug', [

    # letters
    'hathi',

    # dashes
    'hathi-trust',

    # numbers
    'hathi-trust-2016',

])
def test_valid(slug):
    assert slug_is_valid(slug)


@pytest.mark.parametrize('slug', [

    # capitals
    'Hathi-Trust',

    # underscores
    'hathi_trust',

    # spaces
    'hathi trust',

    # padding
    ' hathi-trust ',

    # punctuation
    'hathi-trust!',

])
def test_invalid(slug):
    assert not slug_is_valid(slug)
