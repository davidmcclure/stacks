

import pytest

from sqlalchemy.exc import IntegrityError

from stacks.models import Corpus


pytestmark = pytest.mark.usefixtures('db')


def test_unique(config):

    """
    Block duplicate slugs.
    """

    c1 = Corpus(name='Corpus 1', slug='slug')
    c2 = Corpus(name='Corpus 1', slug='slug')

    config.Session.add(c1)
    config.Session.add(c2)

    with pytest.raises(IntegrityError) as e:
        config.Session.commit()

    assert 'corpus_slug_key' in str(e)
