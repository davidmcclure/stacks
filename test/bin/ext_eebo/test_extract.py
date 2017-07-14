

import pytest

from subprocess import call
from stacks.models import EEBOText

from test.utils import read_yaml


fields = read_yaml(__file__, 'fields.yml')
# texts = read_yaml(__file__, 'texts.yml')


@pytest.fixture(scope='module', autouse=True)
def extract(mpi):
    call(['mpirun', 'bin/ext-eebo.py'])
    call(['mpirun', 'bin/load-metadata.py'])


@pytest.mark.parametrize('idno,fields', fields.items())
def test_fields(idno, fields):

    row = EEBOText.query.get(idno)

    for key, val in fields.items():
        assert getattr(row, key) == val


# @pytest.mark.parametrize('psmid,text', texts.items())
# def test_text(psmid, text, ext_corpus):

    # row = AmficText.query.get(psmid)

    # assert text in ext_corpus.load_text(row)
