

import pytest
import os
import django_rq

from corpus.adapters.eebo.corpus import Corpus


@pytest.fixture(scope='module')
def ingest(django_db_module, redis_module):

    """
    Run ingest jobs.
    """

    path = os.path.join(
        os.path.dirname(__file__),
        'fixtures',
    )

    corpus = Corpus(path)

    corpus.ingest()

    django_rq.get_worker().work(burst=True)
