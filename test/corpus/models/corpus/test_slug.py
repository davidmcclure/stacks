

import pytest

from sqlalchemy.exc import IntegrityError

from stacks.common.singletons import session

from test.corpus.factories import CorpusFactory


pytestmark = pytest.mark.usefixtures('db')


def test_required():

    """
    Block null values.
    """

    CorpusFactory(slug=None)

    with pytest.raises(IntegrityError) as e:
        session.commit()

    assert 'corpus.slug' in str(e)


def test_unique():

    """
    Block duplicate slugs.
    """

    c1 = CorpusFactory(slug='slug')
    c2 = CorpusFactory(slug='slug')

    with pytest.raises(IntegrityError) as e:
        session.commit()

    assert 'corpus.slug' in str(e)


@pytest.mark.parametrize('slug', [

    # letters
    'hathi',

    # dashes
    'hathi-trust',

    # numbers
    'hathi-trust-2016',

])
def test_valid(slug):
    CorpusFactory(slug=slug)


@pytest.mark.parametrize('slug', [

    # capitals
    'Hathi-Trust',

    # underscores
    'hathi_trust',

    # spaces
    'hathi trust',

    # padding
    ' hathi-trust ',

    # punctuation
    'hathi-trust!',

])
def test_invalid(slug):
    with pytest.raises(AssertionError):
        CorpusFactory(slug=slug)
