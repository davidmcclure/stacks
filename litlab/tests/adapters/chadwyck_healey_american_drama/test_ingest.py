

import pytest
import os

from django_rq import get_worker

from litlab.adapters import ChadwyckHealeyAmericanDrama
from corpora.models import Text


pytestmark = pytest.mark.django_db


def test_ingest():

    """
    TODO: Adapter testing harness.
    """

    path = os.path.join(os.path.dirname(__file__), 'fixtures')
    corpus = ChadwyckHealeyAmericanDrama(path)

    corpus.queue()

    get_worker().work(burst=True)

    text = Text.objects.first()

    assert text.title == 'Favelle: Or The Fatal Duel (1809)'
    assert text.creator == 'Adams, C. L. (Charles L.)'
    assert text.date == '1809'
    assert text.type == 'Drama'
