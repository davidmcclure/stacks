

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

    assert Text.objects.filter(

        title   = 'Favelle: Or The Fatal Duel (1809)',
        creator = 'Adams, C. L. (Charles L.)',
        date    = '1809',
        type    = 'Drama',

        plain_text__icontains = 'it is possible that an unguarded word may'

    ).exists()
