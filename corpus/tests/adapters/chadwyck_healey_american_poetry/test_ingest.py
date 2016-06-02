

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


def pytest_generate_tests(metafunc):

    """
    Inject the test cases.
    """

    path = os.path.join(os.path.dirname(__file__), 'texts.yml')

    with open(path) as fh:
        tests = yaml.load(fh)

    metafunc.parametrize('id,fields', tests.items())


def test_ingest(settings, id, fields):

    path = os.path.join(os.path.dirname(__file__), 'fixtures')

    # Patch the corpus path.
    settings.CORPUS_CHADWYCK_HEALEY_AMERICAN_POETRY = path

    # Run the ingest.
    call_command('queue_ingest', 'ChadwyckHealeyAmericanPoetry')
    django_rq.get_worker().work(burst=True)

    corpus = Corpus.objects.get(slug='chadwyck-healey-american-poetry')

    # Check for text.

    text = Text.objects.get(corpus=corpus, identifier=id)

    for key, val in fields.get('equals', {}).items():
        assert getattr(text, key) == val

    for key, val in fields.get('contains', {}).items():
        assert val in getattr(text, key)
