

import pytest

from subprocess import call
from stacks.models import NCCOText, NCCOSubjectHead

from test.utils import read_yaml


@pytest.fixture(scope='module', autouse=True)
def extract(mpi):
    call(['mpirun', 'bin/ext-ncco.py'])
    call(['mpirun', 'bin/load-metadata.py'])


cases = read_yaml(__file__, 'texts.yml')


@pytest.mark.parametrize('psmid,spec', cases.items())
def test_extract(psmid, spec, ext_corpus):

    row = NCCOText.query.get(psmid)

    # Fields
    for key, val in spec['fields'].items():
        assert getattr(row, key) == val

    # Subjects
    for subject in spec.get('subjects', []):
        for sub_field, value in subject['sub_fields'].items():

            assert NCCOSubjectHead.query.filter_by(
                psmid=row.psmid,
                type=subject['type'],
                sub_field=sub_field,
                value=value,
            )

    # Text
    text = ext_corpus.load_text(row)
    assert spec['text'] in text
