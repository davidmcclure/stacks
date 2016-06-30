

import pytest

from sqlalchemy.exc import IntegrityError

from stacks.common import session
from stacks.models import Corpus

from test.factories import CorpusFactory


pytestmark = pytest.mark.usefixtures('db')


def test_required():

    """
    Block null values.
    """

    CorpusFactory(slug=None)

    with pytest.raises(IntegrityError) as e:
        session.commit()

    assert 'slug' in str(e)


def test_unique():

    """
    Block duplicate slugs.
    """

    c1 = CorpusFactory(slug='slug')
    c2 = CorpusFactory(slug='slug')

    with pytest.raises(IntegrityError) as e:
        session.commit()

    assert 'corpus_slug_key' in str(e)