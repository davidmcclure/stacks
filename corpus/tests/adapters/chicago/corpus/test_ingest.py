

import pytest

from corpus.models import Text


pytestmark = pytest.mark.usefixtures('ingest')


@pytest.mark.parametrize('identifier,fields', [

    ('1', dict(
        title='Democracy',
        author_full='Adams, Henry',
        author_first='Henry',
        author_last='Adams',
        year=1880,
        text='After talking of Herbert Spencer for an entire evening with a very',
    )),

    ('3', dict(
        title='The Stillwater tragedy',
        author_full='Aldrich, Thomas Bailey',
        author_first='Thomas Bailey',
        author_last='Aldrich',
        year=1880,
        text='It is close upon daybreak. The great wall of pines and hemlocks',
    )),

    ('13', dict(
        title='Louisiana',
        author_full='Burnett, Frances Hodgson',
        author_first='Frances Hodgson',
        author_last='Burnett',
        year=1880,
        text='Olivia Ferrol leaned back in her chair, her hands folded upon her lap.',
    )),

    ('15', dict(
        title='The Grandissimes',
        author_full='Cable, George Washington',
        author_first='George Washington',
        author_last='Cable',
        year=1880,
        text='It was in the Theatre St. Philippe (they had laid a temporary floor over',
    )),

    ('21', dict(
        title='Hope Mills: or: Between friend and sweetheart',
        author_full='Douglas, Amanda M.',
        author_first='Amanda M.',
        author_last='Douglas',
        year=1880,
        text='THERE is Fred again with his arm around Jack Darcy\'s neck. I declare,',
    )),

])
def test_ingest(identifier, fields):

    text = Text.objects.get(identifier=identifier)

    if 'title' in fields:
        assert text.title == fields['title']

    if 'author_full' in fields:
        assert text.author_full == fields['author_full']

    if 'author_first' in fields:
        assert text.author_first == fields['author_first']

    if 'author_last' in fields:
        assert text.author_last == fields['author_last']

    if 'year' in fields:
        assert text.year == fields['year']

    if 'text' in fields:
        assert fields['text'] in text.plain_text
