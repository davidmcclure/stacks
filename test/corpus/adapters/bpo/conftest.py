

import pytest
import os

from stacks.corpus.adapters.bpo.corpus import Corpus


# TODO: db and redis
@pytest.fixture(scope='module')
def ingest():

    """
    Run ingest jobs.
    """

    path = os.path.join(
        os.path.dirname(__file__),
        'fixtures',
    )

    corpus = Corpus(path)

    corpus.ingest()

    # TODO: Process jobs.
