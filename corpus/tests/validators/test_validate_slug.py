

import pytest

from django.core.exceptions import ValidationError
from corpus.validators import validate_slug


@pytest.mark.parametrize('slug', [

    # Letters:
    'hathi',

    # Dashes:
    'hathi-trust',

    # Numbers:
    'hathi-trust-2016',

])
def test_valid(slug):
    assert validate_slug(slug) is None


@pytest.mark.parametrize('slug', [

    # Capitals:
    'Hathi-Trust',

    # Underscores:
    'hathi_trust',

    # Spaces:
    'hathi trust',

    # Padding:
    ' hathi-trust ',

    # Punctuation:
    'hathi-trust!',

])
def test_invalid(slug):
    with pytest.raises(ValidationError):
        validate_slug(slug)
