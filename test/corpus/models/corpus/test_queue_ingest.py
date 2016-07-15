

import pytest

from stacks.common.singletons import session
from stacks.corpus.models import Corpus, Text

from test.corpus.factories import CorpusFactory, TextFactory


pytestmark = pytest.mark.usefixtures('db')


def test_create_new_corpus():

    """
    A corpus should be created with the passed slug and name.
    """

    Corpus.queue_ingest('test', 'Test Corpus', [], lambda: None)

    corpus = session.query(Corpus).filter_by(slug='test').one()

    assert corpus.name == 'Test Corpus'


def test_replace_existing_corpus():
    pass


def test_delete_existing_corpus():

    """
    If a corpus already exists with the passed slug, delete it.
    """

    old = CorpusFactory(slug='test')

    Corpus.queue_ingest('test', 'Test Corpus', [], lambda: None)

    query = session.query(Corpus).filter_by(slug='test')

    assert query.count() == 1
    assert query.one().id != old.id


def test_delete_existing_texts():

    """
    When an existing corpus is deleted, texts associated with the old corpus
    should also be removed.
    """

    old = CorpusFactory(slug='test')

    TextFactory(corpus=old)
    TextFactory(corpus=old)
    TextFactory(corpus=old)

    Corpus.queue_ingest('test', 'Test Corpus', [], lambda: None)

    assert session.query(Text).filter_by(corpus=old).count() == 0


def test_queue_ingest_jobs():
    pass
