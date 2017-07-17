

import pytest

from subprocess import call
from stacks.models import ChadhPoetryText

from test.utils import read_yaml


fields = read_yaml(__file__, 'fields.yml')
# texts = read_yaml(__file__, 'texts.yml')


@pytest.fixture(scope='module', autouse=True)
def extract(mpi):
    call(['mpirun', 'bin/ext-chadh-poetry.py'])
    call(['mpirun', 'bin/load-metadata.py'])


@pytest.mark.parametrize('idref,fields', fields.items())
def test_fields(idref, fields):

    row = ChadhPoetryText.query.get(idref)

    print(dict(row))

    for key, val in fields.items():
        assert getattr(row, key) == val


# @pytest.mark.parametrize('idref,text', texts.items())
# def test_text(idref, text, ext_corpus):

    # row = ChadhFictionText.query.get(idref)

    # assert text in ext_corpus.load_text(row)
