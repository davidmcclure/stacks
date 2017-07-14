

import pytest

from subprocess import call
from stacks.models import ECCOText, ECCOSubjectHead

from test.utils import read_yaml


fields = read_yaml(__file__, 'fields.yml')
subjects = read_yaml(__file__, 'subjects.yml')
texts = read_yaml(__file__, 'texts.yml')


@pytest.fixture(scope='module', autouse=True)
def extract(mpi):
    call(['mpirun', 'bin/ext-ecco.py'])
    call(['mpirun', 'bin/load-metadata.py'])


@pytest.mark.parametrize('doc_id,fields', fields.items())
def test_fields(doc_id, fields):

    row = ECCOText.query.get(doc_id)

    for key, val in fields.items():
        assert getattr(row, key) == val


@pytest.mark.parametrize('doc_id,subjects', subjects.items())
def test_flex_terms(doc_id, subjects):

    for subject in subjects:
        for sub_field, value in subject['sub_fields'].items():

            query = ECCOSubjectHead.query.filter_by(
                document_id=doc_id,
                type=subject['type'],
                sub_field=sub_field,
                value=value,
            )

            assert query.count() > 0


@pytest.mark.parametrize('doc_id,text', texts.items())
def test_text(doc_id, text, ext_corpus):

    row = ECCOText.query.get(doc_id)

    assert text in ext_corpus.load_text(row)
