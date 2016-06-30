

import pytest

from sqlalchemy.exc import IntegrityError

from stacks.common import session

from test.factories import TextFactory


pytestmark = pytest.mark.usefixtures('db')


def test_required():

    """
    Block null values.
    """

    TextFactory(title=None)

    with pytest.raises(IntegrityError) as e:
        session.commit()

    assert 'title' in str(e)
