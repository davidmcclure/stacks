

import pytest

from subprocess import call


@pytest.fixture(scope='module')
def extract(raw_fixtures):
    call(['mpirun', 'bin/ext-gail-amfic.py'])
