

import pytest

from corpus.models import Text


pytestmark = pytest.mark.usefixtures('ingest')


@pytest.mark.parametrize('identifier,title,author,year,snippet', [

    (
        'brown-dan-angels-and-demons',
        'Angels and Demons',
        'Brown, Dan',
        2000,
        'Antimatter is the most powerful energy source known to man.',
    ),

    (
        'hemingway-ernest-the-sun-also-rises',
        'The Sun Also Rises',
        'Hemingway, Ernest',
        1926,
        'Robert Cohn was once middleweight boxing champion of Princeton.',
    ),

    (
        'dacre-charlotte-zofloya',
        'Zofloya; or, The Moor: A Romance of the Fifteenth Century. In Three Volumes. By Charlotte Dacre, Better Known As Rosa Matilda',
        'Dacre, Charlotte',
        1806,
        'The historian who would wish his lessons',
    ),

    (
        'lennox-charlotte-the-female-quixote-or-the-adventures-of-arabella',
        'The female Quixote; or, the adventures of Arabella. In two volumes. ...',
        'Lennox, Charlotte',
        1752,
        'This extensive Authority could not fail of',
    ),

    (
        'highsmith-patricia-ripley-s-game',
        'Ripley’s Game',
        'Highsmith, Patricia',
        1974,
        'He was sitting in one of the yellow silk armchairs,',
    ),

])
def test_test(identifier, title, author, year, snippet):

    text = Text.objects.get(identifier=identifier)

    assert text.title == title
    assert text.author_name_full == author
    assert text.year == year

    assert snippet in text.plain_text
