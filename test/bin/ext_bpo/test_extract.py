

import pytest

from subprocess import call
from stacks.models import BPOArticle, BPOFlexTerm, BPOContributor

from test.utils import read_yaml


fields = read_yaml(__file__, 'fields.yml')
texts = read_yaml(__file__, 'texts.yml')
flex_terms = read_yaml(__file__, 'flex_terms.yml')
contribs = read_yaml(__file__, 'contribs.yml')


@pytest.fixture(scope='module', autouse=True)
def extract(mpi):
    call(['mpirun', 'bin/ext-bpo.py'])
    call(['mpirun', 'bin/load-metadata.py'])


@pytest.mark.parametrize('record_id,fields', fields.items())
def test_fields(record_id, fields):

    row = BPOArticle.query.get(record_id)

    for key, val in fields.items():
        assert getattr(row, key) == val


@pytest.mark.parametrize('record_id,terms', flex_terms.items())
def test_flex_terms(record_id, terms):

    row = BPOArticle.query.get(record_id)

    for term in terms:

        query = BPOFlexTerm.query.filter_by(
            record_id=row.record_id,
            **term
        )

        assert query.count() == 1


@pytest.mark.parametrize('record_id,contribs', contribs.items())
def test_contributors(record_id, contribs):

    row = BPOArticle.query.get(record_id)

    for contrib in contribs:

        query = BPOContributor.query.filter_by(
            record_id=row.record_id,
            **contrib
        )

        assert query.count() == 1


@pytest.mark.parametrize('record_id,text', texts.items())
def test_text(record_id, text, ext_corpus):

    row = BPOArticle.query.get(record_id)

    assert text in ext_corpus.load_text(row)
