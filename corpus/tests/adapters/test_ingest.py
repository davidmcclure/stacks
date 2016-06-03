

import os
import pytest
import django_rq
import yaml

from django.conf import settings
from django.core.management import call_command

from corpus.models import Text


pytestmark = [
    pytest.mark.django_db,
    pytest.mark.usefixtures('redis'),
]


CORPORA = [
    (
        'chadwyck_healey_american_poetry',
        'CORPUS_CHADWYCK_HEALEY_AMERICAN_POETRY',
        'ChadwyckHealeyAmericanPoetry',
        'chadwyck-healey-american-poetry',
    ),
]


@pytest.fixture(scope='module', autouse=True)
def ingest(_django_db_setup, _django_cursor_wrapper):

    """
    Ingest all testing fixtures.
    """

    with _django_cursor_wrapper:

        for dirname, settings_key, class_name, _ in CORPORA:

            path = os.path.join(
                os.path.dirname(__file__),
                dirname,
                'texts',
            )

        # Patch the corpus path.
        setattr(settings, settings_key, path)

        # Run the ingest.
        call_command('queue_ingest', class_name)
        django_rq.get_worker().work(burst=True)

        print(class_name)


def pytest_generate_tests(metafunc):

    """
    Inject the test cases.
    """

    for dirname, settings_key, class_name, slug in CORPORA:

        path = os.path.join(
            os.path.dirname(__file__),
            dirname,
            'texts.yml',
        )

        with open(path) as fh:
            tests = yaml.load(fh)

        values = [
            (slug, identifier, fields)
            for identifier, fields in tests.items()
        ]

        metafunc.parametrize('slug,identifier,fields', values)


def test_test(slug, identifier, fields):

    """
    Run the field specs.
    """

    text = Text.objects.get(
        corpus__slug=slug,
        identifier=identifier,
    )

    for key, val in fields.get('equals', {}).items():
        assert getattr(text, key) == val

    for key, val in fields.get('contains', {}).items():
        assert val in getattr(text, key)

    for key, val in fields.get('not_contains', {}).items():
        assert val not in getattr(text, key)
