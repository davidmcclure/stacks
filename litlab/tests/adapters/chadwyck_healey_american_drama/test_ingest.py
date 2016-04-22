

import os
import django_rq
import pytest

from litlab.adapters import ChadwyckHealeyAmericanDrama
from django.core.management import call_command
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

    # Run the ingest.
    call_command('queue_ingest', 'ChadwyckHealeyAmericanDrama')
    django_rq.get_worker().work(burst=True)

    assert Text.objects.filter(**query).exists()
