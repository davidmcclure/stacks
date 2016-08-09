

import pytest

from sqlalchemy.exc import IntegrityError

from stacks.singletons import session

from test.corpus.factories import TextFactory


pytestmark = pytest.mark.usefixtures('db')


def test_unique():

    """
    Block duplicate corpus+identifier pairs.
    """

    t1 = TextFactory(corpus='corpus', identifier='1')
    t2 = TextFactory(corpus='corpus', identifier='1')

    with pytest.raises(IntegrityError) as e:
        session.commit()

    assert 'text.corpus' in str(e)
    assert 'text.identifier' in str(e)
