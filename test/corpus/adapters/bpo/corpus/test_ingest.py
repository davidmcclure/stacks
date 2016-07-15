

import pytest

from stacks.common.singletons import session
from stacks.corpus.models import Corpus, Text

from test.utils import read_yaml


pytestmark = pytest.mark.usefixtures('ingest')


cases = read_yaml(__file__, 'ingest.yml')


@pytest.mark.parametrize('identifier,fields', cases.items())
def test_ingest(identifier, fields):

    corpus = (
        session
        .query(Corpus)
        .filter_by(slug='british-periodicals-online')
        .one()
    )

    text = (
        session
        .query(Text)
        .filter_by(corpus=corpus, identifier=identifier)
        .one()
    )

    if 'title' in fields:
        assert text.title == fields['title']

    if 'author_name_full' in fields:
        assert text.author_name_full == fields['author_name_full']

    if 'author_name_first' in fields:
        assert text.author_name_first == fields['author_name_first']

    if 'author_name_last' in fields:
        assert text.author_name_last == fields['author_name_last']

    if 'year' in fields:
        assert text.year == fields['year']

    if 'text' in fields:
        assert fields['text'] in text.plain_text
