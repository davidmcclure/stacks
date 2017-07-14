

import pytest

from subprocess import call
from stacks.models import NCCOText, NCCOSubjectHead

from test.utils import read_yaml


# @pytest.fixture(scope='module', autouse=True)
# def extract(mpi):
    # call(['mpirun', 'bin/ext-ncco.py'])
    # call(['mpirun', 'bin/load-metadata.py'])


# cases = read_yaml(__file__, 'texts.yml')


# @pytest.mark.parametrize('psmid,spec', cases.items())
# def test_extract(psmid, spec, ext_corpus):

    # row = NCCOText.query.get(psmid)

    # # Fields
    # for key, val in spec['fields'].items():
        # assert getattr(row, key) == val

    # # Subjects
    # for subject in spec.get('subjects', []):
        # for sub_field, value in subject['sub_fields'].items():

            # query = NCCOSubjectHead.query.filter_by(
                # psmid=row.psmid,
                # type=subject['type'],
                # sub_field=sub_field,
                # value=value,
            # )

            # assert query.count() == 1

    # # Text
    # text = ext_corpus.load_text(row)
    # assert spec['text'] in text


fields = read_yaml(__file__, 'fields.yml')
subjects = read_yaml(__file__, 'subjects.yml')
texts = read_yaml(__file__, 'texts.yml')


@pytest.fixture(scope='module', autouse=True)
def extract(mpi):
    call(['mpirun', 'bin/ext-ncco.py'])
    call(['mpirun', 'bin/load-metadata.py'])


@pytest.mark.parametrize('psmid,fields', fields.items())
def test_fields(psmid, fields):

    row = NCCOText.query.get(psmid)

    for key, val in fields.items():
        assert getattr(row, key) == val


@pytest.mark.parametrize('psmid,subjects', subjects.items())
def test_flex_terms(psmid, subjects):

    for subject in subjects:
        for sub_field, value in subject['sub_fields'].items():

            query = NCCOSubjectHead.query.filter_by(
                psmid=psmid,
                type=subject['type'],
                sub_field=sub_field,
                value=value,
            )

            assert query.count() > 0


@pytest.mark.parametrize('psmid,text', texts.items())
def test_text(psmid, text, ext_corpus):

    row = NCCOText.query.get(psmid)

    assert text in ext_corpus.load_text(row)
