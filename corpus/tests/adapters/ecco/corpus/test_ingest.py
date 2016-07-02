

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

    ('0002200200', dict(
        title='Abstract of the republics of antiquity.',
        author_name_full='Warrington, W.',
        year=1800,
        text='TOL rectify unstable, or visionary ideas on the subject of politicks:',
    )),

    ('0002300100', dict(
        title='An authentic account of the capture of the Dutch Fleet, consisting of Nine Sail of Men of War, Frigates, &c. at Saldanha Bay, Near the Cape of Good Hope, August 17, 1796. Illustrated with a chart, shewing The Situation of the Dutch Fleet, at the time they surrendered to Vice-Admiral Sir G. K. Elphinstone.',
        author_name_full=None,
        year=1796,
        text='this Day received by the Right Honorable Henry Dundas,',
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
