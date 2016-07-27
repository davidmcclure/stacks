

import pytest
import os

from rq import Worker

from stacks.common.singletons import rq
from stacks.corpus.adapters.gail_amfic.corpus import Corpus


@pytest.fixture(scope='module')
def ingest(db_module, rq_module, fixtures_path):

    """
    Run ingest jobs.
    """

    corpus = Corpus(fixtures_path('gail-amfic'))

    corpus.ingest()

    # Process jobs.
    worker = Worker([rq], connection=rq.connection)
    worker.work(burst=True)
