

import pytest


@pytest.mark.parametrize('author_name,text_name,title', [

    ('King, Stephen', 'Dolores Claiborne', 'Dolores Claiborne'),
    ('King, Stephen', 'It', 'It'),
    ('King, Stephen', 'The Stand', 'The Stand'),
    ('King, Stephen', 'The Talisman', 'The Talisman'),
    ('King, Stephen', 'The Tommyknockers', 'The Tommyknockers'),

    (
        'Kotzwinkle, William',
        'E.T., The Extraterrestrial',
        'E.T., The Extraterrestrial',
    ),

])
def test_title(author_name, text_name, title, get_text):

    text = get_text(author_name, text_name)

    assert text.title() == title
