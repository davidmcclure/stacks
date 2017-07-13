

import pytest

from subprocess import call
from stacks.models import BPOArticle

from test.utils import read_yaml


@pytest.fixture(scope='module', autouse=True)
def extract(mpi):
    call(['mpirun', 'bin/ext-bpo.py'])
    call(['mpirun', 'bin/load-metadata.py'])


cases = read_yaml(__file__, 'texts.yml')


@pytest.mark.parametrize('record_id,spec', cases.items())
def test_extract(record_id, spec, ext_corpus):

    row = BPOArticle.query.get(record_id)
    print(row)

    # # Fields
    # for key, val in spec['fields'].items():
        # assert getattr(row, key) == val

    # # Subjects
    # for subject in spec.get('subjects', []):
        # for sub_field, value in subject['sub_fields'].items():

            # assert NCCOSubjectHead.query.filter_by(
                # type=subject['type'], sub_field=sub_field, value=value,
            # )

    # # Text
    # text = ext_corpus.load_text(row)
    # assert spec['text'] in text
