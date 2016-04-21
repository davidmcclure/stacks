

import os
import django_rq
import pytest

from litlab.adapters import ChadwyckHealeyAmericanDrama
from corpora.models import Text


pytestmark = [
    pytest.mark.django_db,
    pytest.mark.usefixtures('redis'),
]


def test_ingest():

    """
    TODO|dev
    """

    path = os.path.join(os.path.dirname(__file__), 'fixtures')
    corpus = ChadwyckHealeyAmericanDrama(path)

    corpus.queue()

    django_rq.get_worker().work(burst=True)

    text = Text.objects.first()

    assert text.title   == 'Favelle: Or The Fatal Duel (1809)'
    assert text.creator == 'Adams, C. L. (Charles L.)'
    assert text.date    == '1809'
    assert text.type    == 'Drama'

    assert 'it is possible that an unguarded word may' in text.plain_text
