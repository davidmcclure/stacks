

import pytest

from sqlalchemy.exc import IntegrityError

from stacks.common.singletons import session

from test.corpus.factories import CorpusFactory


pytestmark = pytest.mark.usefixtures('db')


def test_required():

    """
    Block null values.
    """

    CorpusFactory(name=None)

    with pytest.raises(IntegrityError) as e:
        session.commit()

    assert 'corpus.name' in str(e)
