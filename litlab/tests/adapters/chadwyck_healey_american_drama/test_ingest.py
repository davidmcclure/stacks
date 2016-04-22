

import os
import django_rq
import pytest

from litlab.adapters import ChadwyckHealeyAmericanDrama
from corpora.models import Text


pytestmark = [
    pytest.mark.django_db,
    pytest.mark.usefixtures('redis'),
]


@pytest.mark.parametrize('query', [

    dict(

        title   = 'Favelle: Or The Fatal Duel (1809)',
        creator = 'Adams, C. L. (Charles L.)',
        date    = '1809',
        type    = 'Drama',

        plain_text__icontains = 'it is possible that an unguarded word may',

    ),

])
def test_ingest(query, settings):

    """
    Test text ingest.
    """

    # Inject fixtures.
    settings.LITLAB_CHADWYCK_HEALEY_AMERICAN_DRAMA = os.path.join(
        os.path.dirname(__file__),
        'fixtures',
    )

    # Queue jobs.
    corpus = ChadwyckHealeyAmericanDrama.from_env()
    corpus.queue()

    # Execute jobs.
    django_rq.get_worker().work(burst=True)

    assert Text.objects.filter(**query).exists()
