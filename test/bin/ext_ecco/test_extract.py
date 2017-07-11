

import pytest

from subprocess import call
from stacks.models import ECCOText, ECCOSubjectHead

from test.utils import read_yaml


@pytest.fixture(scope='module', autouse=True)
def extract(mpi):
    call(['mpirun', 'bin/ext-ecco.py'])
    call(['mpirun', 'bin/load-metadata.py'])


cases = read_yaml(__file__, 'texts.yml')


@pytest.mark.parametrize('doc_id,spec', cases.items())
def test_test(doc_id, spec, ext_corpus):

    row = ECCOText.query.get(doc_id)

    # Fields
    for key, val in spec['fields'].items():
        assert getattr(row, key) == val

    # Subjects
    for subject in spec['subjects']:
        for sub_field, value in subject['sub_fields'].items():

            assert ECCOSubjectHead.query.filter_by(
                type=subject['type'],
                sub_field=sub_field,
                value=value,
            )

    # Text
    text = ext_corpus.load_text(row)
    assert spec['text'] in text

    # TODO: tokens?
