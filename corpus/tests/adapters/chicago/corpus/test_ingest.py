

import pytest

from corpus.models import Text


pytestmark = pytest.mark.usefixtures('ingest')


@pytest.mark.parametrize('identifier,title,author,year,snippet', [

    (
        '1',
        'Democracy',
        'Adams, Henry',
        1880,
        'After talking of Herbert Spencer for an entire evening with a very',
    ),

    (
        '3',
        'The Stillwater tragedy',
        'Aldrich, Thomas Bailey',
        1880,
        'It is close upon daybreak. The great wall of pines and hemlocks',
    ),

    (
        '13',
        'Louisiana',
        'Burnett, Frances Hodgson',
        1880,
        'Olivia Ferrol leaned back in her chair, her hands folded upon her lap.',
    ),

    (
        '15',
        'The Grandissimes',
        'Cable, George Washington',
        1880,
        'It was in the Theatre St. Philippe (they had laid a temporary floor over',
    ),

    (
        '21',
        'Hope Mills: or: Between friend and sweetheart',
        'Douglas, Amanda M.',
        1880,
        'THERE is Fred again with his arm around Jack Darcy\'s neck. I declare,',
    ),

])
def test_test(identifier, title, author, year, snippet):

    text = Text.objects.get(identifier=identifier)

    assert text.title == title
    assert text.author == author
    assert text.year == year

    assert snippet in text.plain_text
