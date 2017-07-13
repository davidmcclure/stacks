

import pytest

from subprocess import call
from stacks.models import BPOArticle, BPOFlexTerm

from test.utils import read_yaml


@pytest.fixture(scope='module', autouse=True)
def extract(mpi):
    call(['mpirun', 'bin/ext-bpo.py'])
    call(['mpirun', 'bin/load-metadata.py'])


cases = read_yaml(__file__, 'texts.yml')


@pytest.mark.parametrize('record_id,spec', cases.items())
def test_extract(record_id, spec, ext_corpus):

    row = BPOArticle.query.get(record_id)

    # Fields
    for key, val in spec['fields'].items():
        assert getattr(row, key) == val

    # Flex terms
    for term in spec['flex_terms']:

        query = BPOFlexTerm.query.filter_by(
            record_id=row.record_id,
            name=term['name'],
            value=term['value'],
        )

        assert query.count() == 1
