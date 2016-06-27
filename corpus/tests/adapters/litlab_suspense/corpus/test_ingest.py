

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

])
def test_test(identifier, title, author, year, snippet):

    text = Text.objects.get(identifier=identifier)

    assert text.title == title
    assert text.author == author
    assert text.year == year

    assert snippet in text.plain_text
