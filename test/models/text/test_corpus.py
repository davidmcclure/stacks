

import pytest

from sqlalchemy.exc import IntegrityError

from stacks.core import session

from test.factories import TextFactory


pytestmark = pytest.mark.usefixtures('db')


def test_required():

    """
    Block null values.
    """

    TextFactory(corpus=None)

    with pytest.raises(IntegrityError) as e:
        session.commit()

    assert 'corpus_id' in str(e)
