

import os
import django_rq
import pytest

from django.conf import settings
from django.core.management import call_command


pytestmark = [
    pytest.mark.django_db,
    pytest.mark.usefixtures('redis'),
]


CORPORA = [
    (
        'chadwyck_healey_american_poetry',
        'CORPUS_CHADWYCK_HEALEY_AMERICAN_POETRY',
        'ChadwyckHealeyAmericanPoetry',
    ),
]


@pytest.fixture(scope='module', autouse=True)
def ingest(_django_db_setup, _django_cursor_wrapper):

    """
    Ingest a corpus.
    """

    with _django_cursor_wrapper:

        for dirname, settings_key, class_name in CORPORA:

            path = os.path.join(
                os.path.dirname(__file__),
                dirname,
                'fixtures',
            )

        # Patch the corpus path.
        setattr(settings, settings_key, path)

        # Run the ingest.
        call_command('queue_ingest', class_name)
        django_rq.get_worker().work(burst=True)

        print(class_name)


def test_test():
    assert True


# def test_ingest(identifier, fields, corpus):

    # """
    # Given a text identifier, a set of field assertions, and the parent corpus,
    # load the text and check the ingested field values.
    # """

    # text = Text.objects.get(corpus=corpus, identifier=identifier)

    # for key, val in fields.get('equals', {}).items():
        # assert getattr(text, key) == val

    # for key, val in fields.get('contains', {}).items():
        # assert val in getattr(text, key)

    # for key, val in fields.get('not_contains', {}).items():
        # assert val not in getattr(text, key)
