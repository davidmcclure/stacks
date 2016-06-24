

import pytest
import django_rq

from corpus.models import Corpus, Text


pytestmark = [
    pytest.mark.django_db,
    pytest.mark.usefixtures('redis'),
]


@pytest.fixture(scope='module', autouse=True)
def ingest(_django_db_setup, _django_cursor_wrapper, corpus):

    """
    Ingest the corpus.
    """

    with _django_cursor_wrapper:
        corpus.ingest()
        django_rq.get_worker().work(burst=True)


@pytest.mark.parametrize('identifier,title,author,year,snippet', [

    (
        'king-stephen-dolores-claiborne',
        'Dolores Claiborne',
        'King, Stephen',
        1992,
        'Gorry! What makes some men so numb?',
    ),

    (
        'king-stephen-it',
        'It',
        'King, Stephen',
        1986,
        'The terror, which would not end for another twenty-eight years—if it ever did end',
    ),

    (
        'king-stephen-the-stand',
        'The Stand',
        'King, Stephen',
        1978,
        'Her husband was deathly pale. His eyes started and bulged from their sockets.',
    ),

    (
        'king-stephen-the-talisman',
        'The Talisman',
        'King, Stephen',
        1984,
        'Jack turned around, looking up the empty beach first to the left, then to the right.',
    ),

    (
        'king-stephen-the-tommyknockers',
        'The Tommyknockers',
        'King, Stephen',
        1987,
        'Well we picked up Harry Truman, floating down from Independence,',
    ),

])
def test_test(identifier, title, author, year, snippet):

    text = Text.objects.get(identifier=identifier)

    assert text.title == title
    assert text.author == author
    assert text.year == year

    assert snippet in text.plain_text
