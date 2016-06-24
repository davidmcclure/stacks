

import pytest


@pytest.mark.parametrize('author_name,text_name,snippet', [

    (
        'King, Stephen',
        'Dolores Claiborne',
        'In the northwestern part of Maine—in the area known as the Lakes District',
    ),

    (
        'King, Stephen',
        'It',
        'The terror, which would not end for another twenty-eight years—if it ever did end',
    ),

    (
        'King, Stephen',
        'The Stand',
        'There are a couple of things you need to know about this version of The Stand right away',
    ),

    (
        'King, Stephen',
        'The Talisman',
        'On September 15th, 1981, a boy named Jack Sawyer stood where the water and land come together',
    ),

    (
        'King, Stephen',
        'The Tommyknockers',
        'Well we picked up Harry Truman, floating down from Independence,',
    ),

    (
        'Matthews, Harry',
        'Tlooth',
        'Center field: Lynn Petomi, dentist, mutilated the mouths of patients.',
    ),

])
def test_title(author_name, text_name, snippet, get_text):

    text = get_text(author_name, text_name)

    assert snippet in text.plain_text()
