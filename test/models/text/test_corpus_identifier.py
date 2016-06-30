

import pytest

from sqlalchemy.exc import IntegrityError

from stacks.common import session
from stacks.models import Corpus

from test.factories import CorpusFactory, TextFactory


pytestmark = pytest.mark.usefixtures('db')


def test_unique():

    """
    Block duplicate corpus+identifier pairs.
    """

    corpus = CorpusFactory()

    t1 = TextFactory(corpus=corpus, identifier='1')
    t2 = TextFactory(corpus=corpus, identifier='1')

    with pytest.raises(IntegrityError) as e:
        session.commit()

    assert 'text_corpus_id_identifier_key' in str(e)
