

import pytest

from sqlalchemy.exc import IntegrityError

from stacks.common.singletons import session

from test.corpus.factories import TextFactory


pytestmark = pytest.mark.usefixtures('db')


def test_required():

    """
    Block null values.
    """

    TextFactory(corpus=None)

    with pytest.raises(IntegrityError) as e:
        session.commit()

    assert 'text.corpus_id' in str(e)
