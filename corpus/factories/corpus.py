

import factory

from corpus.models import Corpus


class CorpusFactory(factory.DjangoModelFactory):


    class Meta:
        model = Corpus


    name = factory.Sequence(
        lambda n: 'Corpus {0}'.format(n)
    )

    slug = factory.Sequence(
        lambda n: 'corpus-{0}'.format(n)
    )
