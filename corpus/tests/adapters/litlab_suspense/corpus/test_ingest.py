

import pytest

from corpus.models import Text


pytestmark = pytest.mark.usefixtures('ingest')


@pytest.mark.parametrize('identifier,fields', [

    ('brown-dan-angels-and-demons', dict(
        title='Angels and Demons',
        author_name_full='Brown, Dan',
        author_name_first='Dan',
        author_name_last='Brown',
        year=2000,
        text='Antimatter is the most powerful energy source known to man.',
    )),

    ('hemingway-ernest-the-sun-also-rises', dict(
        title='The Sun Also Rises',
        author_name_full='Hemingway, Ernest',
        author_name_first='Ernest',
        author_name_last='Hemingway',
        year=1926,
        text='Robert Cohn was once middleweight boxing champion of Princeton.',
    )),

    ('dacre-charlotte-zofloya', dict(
        title='Zofloya; or, The Moor: A Romance of the Fifteenth Century. In Three Volumes. By Charlotte Dacre, Better Known As Rosa Matilda',
        author_name_full='Dacre, Charlotte',
        author_name_first='Charlotte',
        author_name_last='Dacre',
        year=1806,
        text='The historian who would wish his lessons',
    )),

    ('lennox-charlotte-the-female-quixote-or-the-adventures-of-arabella', dict(

        title='The female Quixote; or, the adventures of Arabella. In two volumes. ...',
        author_name_full='Lennox, Charlotte',

        # Missing names in metadata file.
        author_name_first=None,
        author_name_last=None,

        year=1752,
        text='This extensive Authority could not fail of',

    )),

    ('highsmith-patricia-ripley-s-game', dict(
        title='Ripley’s Game',
        author_name_full='Highsmith, Patricia',
        author_name_first='Patricia',
        author_name_last='Highsmith',
        year=1974,
        text='He was sitting in one of the yellow silk armchairs,',
    )),

    ('schwartz-alvin-scary-stories-to-tell-in-the-dark', dict(
        title='Scary Stories to Tell in the Dark',
        author_name_full='Schwartz, Alvin',
        author_name_first='Alvin',
        author_name_last='Schwartz',
        year=1981,
        text='Pioneers used to entertain themselves by telling scary stories.',
    )),

    # Metadata file with empty lines.
    ('utterson-sarah-elizabeth-fantasmagoriana', dict(
        title='Fantasmagoriana',
        author_name_full='Utterson, Sarah Elizabeth',
        author_name_first='Sarah',
        author_name_last='Utterson',
        year=1813,
        text='As was usual with young men of rank, he had visited several universities;',
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
