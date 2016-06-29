

import pytest

from sqlalchemy.exc import IntegrityError

from stacks import session
from stacks.models import Corpus

from test.factories import CorpusFactory


pytestmark = pytest.mark.usefixtures('db')


def test_unique(config):

    """
    Block duplicate slugs.
    """

    c1 = CorpusFactory(slug='slug')
    c2 = CorpusFactory(slug='slug')

    with pytest.raises(IntegrityError) as e:
        session.commit()

    assert 'corpus_slug_key' in str(e)
