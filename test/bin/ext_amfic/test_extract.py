

import pytest

from subprocess import call
from stacks.models import AmficText

from test.utils import read_yaml


@pytest.fixture(scope='module', autouse=True)
def extract(mpi):
    call(['mpirun', 'bin/ext-amfic.py'])
    call(['mpirun', 'bin/load-metadata.py'])


cases = read_yaml(__file__, 'texts.yml')


@pytest.mark.parametrize('psmid,spec', cases.items())
def test_test(psmid, spec, ext_corpus):

    row = AmficText.query.get(psmid)

    # Fields
    for key, val in spec['fields'].items():
        assert getattr(row, key) == val

    # Text
    text = ext_corpus.load_text(row)
    assert spec['text'] in text