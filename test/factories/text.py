

import factory

from datetime import datetime as dt

from stacks.utils import git_rev
from stacks import session
from stacks.metadata.models import Text


class TextFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        sqlalchemy_session = session
        model = Text

    path = factory.Sequence(
        lambda n: '/ext/path{0}'.format(n)
    )

    version = git_rev()

    created_at = dt.now()

    corpus = 'corpus'

    identifier = factory.Sequence(
        lambda n: n
    )

    title = factory.Sequence(
        lambda n: 'Text {0}'.format(n)
    )

    author_full = 'Wharton, Edith'

    author_first = 'Edith'

    author_last = 'Wharton'

    year = 1900
