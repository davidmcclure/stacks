

import pytest

from sqlalchemy.exc import IntegrityError

from stacks.models import Corpus


pytestmark = pytest.mark.usefixtures('db')


def test_unique(config):

    """
    Block duplicate slugs.
    """

    with config.get_session() as session:

        c1 = Corpus(name='Corpus 1', slug='slug')
        c2 = Corpus(name='Corpus 1', slug='slug')

        session.add(c1)
        session.add(c2)

        session.commit()
