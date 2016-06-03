

import os
import django_rq
import yaml
import pytest

from django.conf import settings
from django.core.management import call_command

from corpus.models import Text


pytestmark = [
    pytest.mark.django_db,
    pytest.mark.usefixtures('redis'),
]


@pytest.fixture(scope='module', autouse=True)
def ingest(_django_db_setup, _django_cursor_wrapper):

    """
    Run the corpus ingest.
    """

    path = os.path.join(os.path.dirname(__file__), 'texts')

    # Patch the corpus path.
    settings.CORPUS_CHADWYCK_HEALEY_AMERICAN_POETRY = path

    with _django_cursor_wrapper:

        # Run the ingest.
        call_command('queue_ingest', 'ChadwyckHealeyAmericanPoetry')
        django_rq.get_worker().work(burst=True)


def pytest_generate_tests(metafunc):

    """
    Inject the test cases.
    """

    path = os.path.join(os.path.dirname(__file__), 'texts.yml')

    with open(path) as fh:
        tests = yaml.load(fh)

    metafunc.parametrize('identifier,fields', tests.items())


def test_ingest(identifier, fields):

    """
    Assert the field specs.
    """

    text = Text.objects.get(
        corpus__slug='chadwyck-healey-american-poetry',
        identifier=identifier,
    )

    for key, val in fields.get('equals', {}).items():
        assert getattr(text, key) == val

    for key, val in fields.get('contains', {}).items():
        assert val in getattr(text, key)

    for key, val in fields.get('not_contains', {}).items():
        assert val not in getattr(text, key)
