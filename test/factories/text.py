

import factory

from stacks.common import session
from stacks.models import Text

from test.factories import CorpusFactory


class TextFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        sqlalchemy_session = session
        model = Text

    corpus = factory.SubFactory(CorpusFactory)

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

    plain_text = 'To keep a kind of republic of the spirit...'
