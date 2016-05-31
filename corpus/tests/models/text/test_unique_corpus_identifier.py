

import pytest

from corpus.factories import CorpusFactory, TextFactory
from django.db.utils import IntegrityError


pytestmark = pytest.mark.django_db


def test_block_duplicate_identifiers_in_the_same_corpus():

    """
    Within a given corpus, identifiers must be unique.
    """

    corpus = CorpusFactory.create()

    TextFactory.create(corpus=corpus, identifier='1')

    with pytest.raises(IntegrityError):
        TextFactory.create(corpus=corpus, identifier='1')


def test_allow_duplicate_identifiers_in_different_corpora():

    """
    Texts in different corpora can have the same identifiers.
    """

    corpus1 = CorpusFactory.create()
    corpus2 = CorpusFactory.create()

    TextFactory.create(corpus=corpus1, identifier='1')
    TextFactory.create(corpus=corpus2, identifier='1')
