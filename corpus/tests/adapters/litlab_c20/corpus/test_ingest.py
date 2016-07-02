

import pytest

from corpus.models import Text


pytestmark = pytest.mark.usefixtures('ingest')


@pytest.mark.parametrize('identifier,fields', [

    ('king-stephen-dolores-claiborne', dict(
        title='Dolores Claiborne',
        author_name_full='King, Stephen',
        author_name_first='Stephen',
        author_name_last='King',
        year=1992,
        text='Gorry! What makes some men so numb?',
    )),

    ('king-stephen-it', dict(
        title='It',
        author_name_full='King, Stephen',
        author_name_first='Stephen',
        author_name_last='King',
        year=1986,
        text='The terror, which would not end for another twenty-eight years—if it ever did end',
    )),

    ('king-stephen-the-stand', dict(
        title='The Stand',
        author_name_full='King, Stephen',
        author_name_first='Stephen',
        author_name_last='King',
        year=1978,
        text='Her husband was deathly pale. His eyes started and bulged from their sockets.',
    )),

    ('king-stephen-the-talisman', dict(
        title='The Talisman',
        author_name_full='King, Stephen',
        author_name_first='Stephen',
        author_name_last='King',
        year=1984,
        text='Jack turned around, looking up the empty beach first to the left, then to the right.',
    )),

    ('king-stephen-the-tommyknockers', dict(
        title='The Tommyknockers',
        author_name_full='King, Stephen',
        author_name_first='Stephen',
        author_name_last='King',
        year=1987,
        text='Well we picked up Harry Truman, floating down from Independence,',
    )),

    ('kotzwinkle-william-e-t-the-extraterrestrial', dict(
        title='E.T., The Extraterrestrial',
        author_name_full='Kotzwinkle, William',
        author_name_first='William',
        author_name_last='Kotzwinkle',
        year=1982,
        text='The spaceship floated gently, anchored by a beam of lavender light to the earth below.',
    )),

    ('tolkien-j-r-r-the-lord-of-the-rings', dict(
        title='The Lord of the Rings',
        author_name_full='Tolkien, J.R.R.',
        author_name_first='John',
        author_name_last='Tolkien',
        year=1937,
        text='Three Rings for the Elven-kings under the sky,',
    )),

    ('matthews-harry-tlooth', dict(
        title='Tlooth',
        author_name_full='Matthews, Harry',
        author_name_first='Harry',
        author_name_last='Matthews',
        year=1966,
        text='Center field: Lynn Petomi, dentist, mutilated the mouths of patients.',
    )),

])
def test_ingest(identifier, fields):

    text = Text.objects.get(identifier=identifier)

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
