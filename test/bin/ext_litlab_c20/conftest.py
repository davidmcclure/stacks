

import pytest

from subprocess import call


@pytest.fixture(scope='module')
def extract(mpi):
    call(['mpirun', 'bin/ext-litlab-c20.py'])
