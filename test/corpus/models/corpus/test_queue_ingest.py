

import pytest

from stacks.common.singletons import session, rq
from stacks.corpus.models import Corpus, Text

from test.corpus.factories import CorpusFactory, TextFactory


pytestmark = pytest.mark.usefixtures('db', 'rq')


# Test job function.
def job(): pass


def test_queue_ingest_jobs_with_scalar_args():

    """
    RQ jobs should be queued for each of the passed arguments. When the
    arguments are scalars, they should be passed in *args.
    """

    args = [
        '/path/1',
        '/path/2',
        '/path/3',
    ]

    corpus = CorpusFactory()

    corpus.queue_ingest(job, args)

    assert rq.count == 3

    for i, arg in enumerate(args):
        assert rq.jobs[i].args == (corpus.id, arg)
        assert rq.jobs[i].func == job


def test_queue_ingest_jobs_with_dict_args():

    """
    When the arguments are dictionaries, they should be passed as **kwargs.
    """

    args = [
        dict(zip_path='1.zip', xml_path='1.xml'),
        dict(zip_path='2.zip', xml_path='2.xml'),
        dict(zip_path='3.zip', xml_path='3.xml'),
    ]

    corpus = CorpusFactory()

    corpus.queue_ingest(job, args)

    assert rq.count == 3

    for i, arg in enumerate(args):
        assert rq.jobs[i].args == (corpus.id,)
        assert rq.jobs[i].kwargs == arg
        assert rq.jobs[i].func == job
