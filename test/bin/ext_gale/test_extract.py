

import pytest

from subprocess import call
from stacks.models import GaleText

from test.utils import read_yaml


@pytest.fixture(scope='module', autouse=True)
def extract(mpi):
    call(['mpirun', 'bin/ext-gale.py'])
    call(['mpirun', 'bin/load-metadata.py'])


cases = read_yaml(__file__, 'texts.yml')


@pytest.mark.parametrize('psmid,spec', cases.items())
def test_test(psmid, spec, ext_corpus):

    row = GaleText.query.get(psmid)
    print(row)
