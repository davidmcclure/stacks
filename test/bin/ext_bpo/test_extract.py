

import pytest

from subprocess import call
from stacks.models import BPOArticle, BPOFlexTerm, BPOContributor

from test.utils import read_yaml


@pytest.fixture(scope='module', autouse=True)
def extract(mpi):
    call(['mpirun', 'bin/ext-bpo.py'])
    call(['mpirun', 'bin/load-metadata.py'])


cases = read_yaml(__file__, 'texts.yml')


# @pytest.mark.parametrize('record_id,spec', cases.items())
# def test_extract(record_id, spec, ext_corpus):

    # row = BPOArticle.query.get(record_id)

    # # TODO: Parametrize everything as separate tests?

    # # Fields
    # for key, val in spec['fields'].items():
        # assert getattr(row, key) == val

    # # Flex terms
    # for term in spec['flex_terms']:

        # query = BPOFlexTerm.query.filter_by(
            # record_id=row.record_id,
            # **term
        # )

        # assert query.count() == 1

    # # Contributors
    # for contrib in spec['contributors']:

        # query = BPOContributor.query.filter_by(
            # record_id=row.record_id,
            # **contrib
        # )

        # assert query.count() == 1

    # # Text
    # text = ext_corpus.load_text(row)
    # assert spec['text'] in text


fields = read_yaml(__file__, 'fields.yml')

@pytest.mark.parametrize('record_id,fields', fields.items())
def test_fields(record_id, fields):

    row = BPOArticle.query.get(record_id)

    for key, val in fields.items():
        assert getattr(row, key) == val


flex_terms = read_yaml(__file__, 'flex_terms.yml')

@pytest.mark.parametrize('record_id,terms', flex_terms.items())
def test_flex_terms(record_id, terms):

    row = BPOArticle.query.get(record_id)

    for term in terms:

        query = BPOFlexTerm.query.filter_by(
            record_id=row.record_id,
            **term
        )

        assert query.count() == 1


contribs = read_yaml(__file__, 'contributors.yml')

@pytest.mark.parametrize('record_id,contribs', contribs.items())
def test_contributors(record_id, contribs):

    row = BPOArticle.query.get(record_id)

    for contrib in contribs:

        query = BPOContributor.query.filter_by(
            record_id=row.record_id,
            **contrib
        )

        assert query.count() == 1
