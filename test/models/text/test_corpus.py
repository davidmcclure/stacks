

import pytest

from sqlalchemy.exc import IntegrityError

from stacks.common import session
from stacks.models import Corpus

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