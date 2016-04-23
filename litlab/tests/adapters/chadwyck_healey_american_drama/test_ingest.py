

import os
import django_rq
import pytest

from litlab.adapters import ChadwyckHealeyAmericanDrama
from django.core.management import call_command
from corpus.models import Text


pytestmark = [
    pytest.mark.django_db,
    pytest.mark.usefixtures('redis'),
]


@pytest.mark.parametrize('query', [

    dict(

        title   = 'Favelle: Or The Fatal Duel (1809)',
        author  = 'Adams, C. L. (Charles L.)',
        year    = 1809,

        plain_text__icontains = 'it is possible that an unguarded word may',

    ),

    dict(

        title   = 'Vanity; or, A Lord in Philadelphia (1854)',
        author  = 'Addis, J. B.',
        year    = 1854,

        plain_text__icontains = 'Of course, I sent a liveried servant',

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

    # Run the ingest.
    call_command('queue_ingest', 'ChadwyckHealeyAmericanDrama')
    django_rq.get_worker().work(burst=True)

    assert Text.objects.filter(**query).exists()
