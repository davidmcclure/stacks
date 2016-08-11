

import factory

from datetime import datetime as dt

from stacks.singletons import session, version
from stacks.models import Text


class TextFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        sqlalchemy_session = session
        model = Text

    version = version

    created_at = dt.now()

    corpus = 'corpus'

    identifier = factory.Sequence(
        lambda n: n
    )

    title = factory.Sequence(
        lambda n: 'Text {0}'.format(n)
    )

    author_name_full = 'Wharton, Edith'

    author_name_first = 'Edith'

    author_name_last = 'Wharton'

    year = 1900
