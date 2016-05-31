

import os
import django_rq
import pytest
import yaml

from django.core.management import call_command
from corpus.adapters import ChadwyckHealeyAmericanDrama
from corpus.models import Text


pytestmark = [
    pytest.mark.django_db,
    pytest.mark.usefixtures('redis'),
]


def test_ingest(settings):

    dirname = os.path.dirname(__file__)

    # Inject fixtures.
    settings.CORPUS_CHADWYCK_HEALEY_AMERICAN_POETRY = os.path.join(
        dirname, 'fixtures',
    )

    # Run the ingest.
    call_command('queue_ingest', 'ChadwyckHealeyAmericanPoetry')
    django_rq.get_worker().work(burst=True)

    # Check for texts.
    with open(os.path.join(dirname, 'texts.yml')) as fh:

        texts = yaml.load(fh)

        for text in texts:
            assert Text.objects.filter(**text).exists()
