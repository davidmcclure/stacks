

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

])
def test_test(identifier, title, author, year, snippet):

    text = Text.objects.get(identifier=identifier)

    assert text.title == title
    assert text.author == author
    assert text.year == year

    assert snippet in text.plain_text
