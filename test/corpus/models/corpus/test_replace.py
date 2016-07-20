

import pytest

from stacks.corpus.models import Corpus, Text

from test.corpus.factories import CorpusFactory, TextFactory


pytestmark = pytest.mark.usefixtures('db')


def test_create_new_corpus():

    """
    A corpus should be created with the passed slug and name.
    """

    Corpus.replace(slug='test', name='Test Corpus')

    corpus = Corpus.get_by(slug='test')

    assert corpus.name == 'Test Corpus'


def test_replace_existing_corpus():

    """
    If a corpus already exists with the passed slug, delete it.
    """

    old = CorpusFactory(slug='test')

    Corpus.replace(slug='test', name='Test Corpus')

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

    Corpus.replace(slug='test', name='Test Corpus')

    assert Text.query.filter_by(corpus=old).count() == 0
