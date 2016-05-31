

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

    # Read the YAML cases.
    with open(os.path.join(dirname, 'texts.yml')) as fh:
        texts = yaml.load(fh)

    # Check for text.
    for id, params in texts.items():
        for key, val in params.items():
            assert Text.objects.filter(identifier=id, **{key: val})
