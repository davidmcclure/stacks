

import os
import django_rq
import pytest
import yaml

from django.core.management import call_command

from corpus.models import Text, Corpus


pytestmark = [
    pytest.mark.django_db,
    pytest.mark.usefixtures('redis'),
]


def test_ingest(settings):

    dirname = os.path.dirname(__file__)

    fixtures_path = os.path.join(dirname, 'fixtures')
    text_path = os.path.join(dirname, 'texts.yml')

    # Inject fixtures.
    settings.CORPUS_CHADWYCK_HEALEY_AMERICAN_POETRY = fixtures_path

    # Run the ingest.
    call_command('queue_ingest', 'ChadwyckHealeyAmericanPoetry')
    django_rq.get_worker().work(burst=True)

    corpus = Corpus.objects.get(slug='chadwyck-healey-american-poetry')

    # Read the YAML cases.
    with open(text_path) as fh:
        texts = yaml.load(fh)

    # Check for texts.
    for id, fields in texts.items():

        text = Text.objects.get(corpus=corpus, identifier=id)

        for key, val in fields.get('equals', {}).items():
            assert getattr(text, key) == val

        for key, val in fields.get('contains', {}).items():
            assert val in getattr(text, key)
