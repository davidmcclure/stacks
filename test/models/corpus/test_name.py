

import pytest

from sqlalchemy.exc import IntegrityError

from stacks.common import session

from test.factories import CorpusFactory


pytestmark = pytest.mark.usefixtures('db')


def test_required():

    """
    Block null values.
    """

    CorpusFactory(name=None)

    with pytest.raises(IntegrityError) as e:
        session.commit()

    assert 'name' in str(e)
