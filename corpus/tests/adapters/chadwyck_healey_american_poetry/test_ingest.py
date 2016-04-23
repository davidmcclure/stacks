

import os
import django_rq
import pytest

from django.core.management import call_command
from corpus.adapters import ChadwyckHealeyAmericanPoetry
from corpus.models import Text


pytestmark = [
    pytest.mark.django_db,
    pytest.mark.usefixtures('redis'),
]


@pytest.mark.parametrize('query', [

    dict(

        title   = 'THE COLUMBIAD. A Poem, WITH THE LAST CORRECTIONS OF THE AUTHOR.',
        author  = 'Barlow, Joel, 1754-1812',
        year    = 1825,

        plain_text__icontains = 'Che quel poco dara lunga memoria',

    ),

])
def test_ingest(query, settings):

    # Inject fixtures.
    settings.CORPUS_CHADWYCK_HEALEY_AMERICAN_POETRY = os.path.join(
        os.path.dirname(__file__),
        'fixtures',
    )

    # Run the ingest.
    call_command('queue_ingest', 'ChadwyckHealeyAmericanPoetry')
    django_rq.get_worker().work(burst=True)

    assert Text.objects.filter(**query).exists()
