

import pytest
import os

from rq import SimpleWorker

from stacks.common.singletons import rq
from stacks.corpus.adapters.litlab_c20.corpus import Corpus


@pytest.fixture(scope='module')
def ingest(db_module, rq_module):

    """
    Run ingest jobs.
    """

    path = os.path.join(
        os.path.dirname(__file__),
        'fixtures',
    )

    corpus = Corpus(path)

    corpus.ingest()

    # Process jobs.
    worker = SimpleWorker([rq], connection=rq.connection)
    worker.work(burst=True)
