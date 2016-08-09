

import factory

from stacks.singletons import session
from stacks.models import Text


class TextFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        sqlalchemy_session = session
        model = Text

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
