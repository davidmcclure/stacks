

import pytest

from stacks.common.singletons import session, rq
from stacks.corpus.models import Corpus, Text

from test.corpus.factories import CorpusFactory, TextFactory


pytestmark = pytest.mark.usefixtures('db', 'rq')


# TODO: Make this an instance method on Corpus?


# Test job function.
def job(): pass


def test_create_new_corpus():

    """
    A corpus should be created with the passed slug and name.
    """

    Corpus.queue_ingest('test', 'Test Corpus', [], job)

    corpus = Corpus.get_by(slug='test')

    assert corpus.name == 'Test Corpus'


def test_replace_existing_corpus():

    """
    If a corpus already exists with the passed slug, delete it.
    """

    old = CorpusFactory(slug='test')

    Corpus.queue_ingest('test', 'Test Corpus', [], job)

    query = Corpus.query.filter_by(slug='test')

    assert query.count() == 1
    assert query.one().id != old.id


def test_delete_existing_texts():

    """
    When an existing corpus is replaced, texts associated with the old corpus
    should also be removed.
    """

    old = CorpusFactory(slug='test')

    TextFactory(corpus=old)
    TextFactory(corpus=old)
    TextFactory(corpus=old)

    Corpus.queue_ingest('test', 'Test Corpus', [], job)

    assert Text.query.filter_by(corpus=old).count() == 0


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

    Corpus.queue_ingest('test', 'Test Corpus', args, job)

    corpus = Corpus.get_by(slug='test')

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

    Corpus.queue_ingest('test', 'Test Corpus', args, job)

    corpus = Corpus.get_by(slug='test')

    assert rq.count == 3

    for i, arg in enumerate(args):
        assert rq.jobs[i].args == (corpus.id,)
        assert rq.jobs[i].kwargs == arg
        assert rq.jobs[i].func == job
