

import factory

from stacks import session
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
