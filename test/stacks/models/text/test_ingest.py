

import pytest

from datetime import datetime as dt

from stacks.json_text import JSONText
from stacks.models import Text


pytestmark = pytest.mark.usefixtures('db')


def test_ingest(json_corpus):

    """
    Text.ingest() should load texts from the ENV-defined corpus.
    """

    now = dt.now()

    t1 = JSONText(dict(
        corpus='corpus1',
        identifier='identifier1',
        title='title1',
        plain_text='text1',
        author_name_full='last1, first1',
        author_name_first='first1',
        author_name_last='last1',
        year=1901,
    ))

    t2 = JSONText(dict(
        corpus='corpus2',
        identifier='identifier2',
        title='title2',
        plain_text='text2',
        author_name_full='last2, first2',
        author_name_first='first2',
        author_name_last='last2',
        year=1902,
    ))

    t3 = JSONText(dict(
        corpus='corpus3',
        identifier='identifier3',
        title='title3',
        plain_text='text3',
        author_name_full='last3, first3',
        author_name_first='first3',
        author_name_last='last3',
        year=1903,
    ))

    json_corpus.insert_text(t1)
    json_corpus.insert_text(t2)
    json_corpus.insert_text(t3)

    Text.ingest()

    assert Text.query.count() == 3

    for text in [t1, t2, t3]:

        # Load the database row.
        row = Text.get_by(
            corpus=text.corpus,
            identifier=text.identifier,
        )

        # Get keys, minus the id.
        keys = [
            k for k in row.asdict().keys()
            if k != 'id'
        ]

        # Row should mirror JSON.
        for key in keys:
            assert getattr(row, key) == getattr(text, key)
