

import pytest

from corpus.factories import CorpusFactory
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError


pytestmark = [

    pytest.mark.django_db,

    pytest.mark.parametrize('factory', [
        CorpusFactory,
    ]),

]


def test_validate_slug_format(factory):

    """
    Block invalid formats.
    """

    model = factory.build(slug='invalid_slug')

    with pytest.raises(ValidationError) as e:
        model.full_clean()
        assert 'slug' in e.message_dict


def test_enforce_uniqueness(factory):

    """
    Block duplicate values.
    """

    factory.create(slug='slug')

    with pytest.raises(IntegrityError) as e:
        factory.create(slug='slug')
        assert 'slug' in e.message_dict
