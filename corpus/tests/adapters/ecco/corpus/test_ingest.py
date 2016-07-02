

import pytest

from corpus.models import Text


pytestmark = pytest.mark.usefixtures('ingest')


@pytest.mark.parametrize('identifier,fields', [

    ('0031300100', dict(
        title='Bibliotheca topographica Anglicana: or, a new and compleat catalogue of all the books extant relating to the antiquity, description, and natural history of England, the Counties thereof, &c. to the present year 1736, Alphabetically digested in an easy Method; giving an Account of their various Editions, Dates, and Prices, and wherein they differ. Compil\'d by John Worrall.',
        author_name_full='Worrall, John',
        year=1736,
        text='beautifully Engraven on Copper Plates and Coloured from the Life,',
    )),

    ('0031300200', dict(
        title='A catalogue of books printed for, and sold by Charles Dilly, in London. All the Articles in the following Catalogue are sold at the Prices marked bound; unless otherwise expressed.',
        author_name_full='Dilly, Charles',
        year=1787,
        text='on the Doses. and EfieOs of Medi- cines;',
    )),

])
def test_ingest(identifier, fields):

    text = Text.objects.get(identifier=identifier)

    if 'title' in fields:
        assert text.title == fields['title']

    if 'author_name_full' in fields:
        assert text.author_name_full == fields['author_name_full']

    if 'year' in fields:
        assert text.year == fields['year']

    if 'text' in fields:
        assert fields['text'] in text.plain_text
