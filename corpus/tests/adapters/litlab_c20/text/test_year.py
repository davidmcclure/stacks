

import pytest


@pytest.mark.parametrize('author_name,text_name,year', [

    ('King, Stephen', 'Dolores Claiborne', 1992),
    ('King, Stephen', 'It', 1986),
    ('King, Stephen', 'The Stand', 1978),
    ('King, Stephen', 'The Talisman', 1984),
    ('King, Stephen', 'The Tommyknockers', 1987),

    # If the year is a range, take first year.
    ('Tolkien, J.R.R.', 'The Lord of the Rings', 1937),

])
def test_title(author_name, text_name, year, get_text):

    text = get_text(author_name, text_name)

    assert text.year() == year
