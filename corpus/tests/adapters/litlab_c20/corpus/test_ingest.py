

import pytest
import django_rq

from corpus.models import Corpus, Text


pytestmark = [
    pytest.mark.django_db,
    pytest.mark.usefixtures('redis'),
]


def test_test(corpus):

    corpus.ingest()

    django_rq.get_worker().work(burst=True)

    assert Corpus.objects.count() == 1
    assert Text.objects.count() == 5
