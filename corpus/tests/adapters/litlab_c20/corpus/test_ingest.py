

import pytest

from corpus.models import Text


pytestmark = pytest.mark.usefixtures('ingest')


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

    (
        'kotzwinkle-william-e-t-the-extraterrestrial',
        'E.T., The Extraterrestrial',
        'Kotzwinkle, William',
        1982,
        'The spaceship floated gently, anchored by a beam of lavender light to the earth below.',
    ),

    (
        'tolkien-j-r-r-the-lord-of-the-rings',
        'The Lord of the Rings',
        'Tolkien, J.R.R.',
        1937,
        'Three Rings for the Elven-kings under the sky,',
    ),

    (
        'matthews-harry-tlooth',
        'Tlooth',
        'Matthews, Harry',
        1966,
        'Center field: Lynn Petomi, dentist, mutilated the mouths of patients.',
    ),

])
def test_test(identifier, title, author, year, snippet):

    text = Text.objects.get(identifier=identifier)

    assert text.title == title
    assert text.author_full == author
    assert text.year == year

    assert snippet in text.plain_text
