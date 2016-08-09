

import pytest

from sqlalchemy.exc import IntegrityError

from stacks.singletons import session

from test.factories import TextFactory


pytestmark = pytest.mark.usefixtures('db')


def test_required():

    """
    Block null values.
    """

    TextFactory(corpus=None)

    with pytest.raises(IntegrityError) as e:
        session.commit()

    assert 'text.corpus' in str(e)
