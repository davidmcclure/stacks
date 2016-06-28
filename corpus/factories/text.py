

import factory

from corpus.factories import CorpusFactory
from corpus.models import Text


class TextFactory(factory.DjangoModelFactory):

    class Meta:
        model = Text

    corpus = factory.SubFactory(CorpusFactory)

    identifier = factory.Sequence(
        lambda n: 'text-{0}'.format(n)
    )
