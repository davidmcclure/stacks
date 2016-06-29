

import factory

from stacks import session
from stacks.models import Corpus


class CorpusFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        sqlalchemy_session = session
        model = Corpus

    id = factory.Sequence(
        lambda n: n
    )

    name = factory.Sequence(
        lambda n: 'Corpus {0}'.format(n)
    )

    slug = factory.Sequence(
        lambda n: 'corpus-{0}'.format(n)
    )
