

import factory

from corpora.models import Corpus


class CorpusFactory(factory.DjangoModelFactory):


    class Meta:
        model = Corpus


    name = factory.Sequence(
        lambda n: 'Corpus {0}'.format(n)
    )
