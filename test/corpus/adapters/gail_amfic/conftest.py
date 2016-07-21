

import pytest
import os

from rq import Worker

from stacks.common.singletons import rq
from stacks.corpus.adapters.gail_amfic.corpus import Corpus


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
    worker = Worker([rq], connection=rq.connection)
    worker.work(burst=True)
