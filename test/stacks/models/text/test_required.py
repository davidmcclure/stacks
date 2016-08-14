

import pytest

from sqlalchemy.exc import IntegrityError

from stacks import session

from test.factories import TextFactory


pytestmark = pytest.mark.usefixtures('db')


@pytest.mark.parametrize('field', [
    'version',
    'created_at',
    'corpus',
    'identifier',
    'title',
])
def test_required(field):

    """
    Block null values.
    """

    TextFactory(**{field: None})

    with pytest.raises(IntegrityError) as e:
        session.commit()

    assert 'text.{0}'.format(field) in str(e)
