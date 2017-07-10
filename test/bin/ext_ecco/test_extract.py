

import pytest

from subprocess import call
from stacks.metadata.models import ECCOText, ECCOSubjectHead

from test.utils import read_yaml


@pytest.fixture(scope='module', autouse=True)
def extract(mpi):
    call(['mpirun', 'bin/ext-ecco.py'])
    call(['mpirun', 'bin/load-metadata.py'])


cases = read_yaml(__file__, 'texts.yml')


@pytest.mark.parametrize('doc_id,spec', cases.items())
def test_test(doc_id, spec):

    text = ECCOText.query.get(doc_id)

    # Fields
    for key, val in spec['fields'].items():
        assert getattr(text, key) == val

    # Subjects
    for subject in spec['subjects']:
        for sub_field, value in subject['sub_fields'].items():

            assert ECCOSubjectHead.query.filter_by(
                type=subject['type'],
                sub_field=sub_field,
                value=value,
            )


# @pytest.mark.parametrize('identifier,fields', cases.items())
# def test_extract(identifier, fields, ext_corpus):

    # text = ext_corpus.get_text('ecco', identifier)

    # if 'title' in fields:
        # assert text.title == fields['title']

    # if 'author_full' in fields:
        # assert text.author_full == fields['author_full']

    # if 'year' in fields:
        # assert text.year == fields['year']

    # if 'text' in fields:
        # assert fields['text'] in text.plain_text
