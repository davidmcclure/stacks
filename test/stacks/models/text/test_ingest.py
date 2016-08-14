

import pytest

from datetime import datetime as dt

from stacks.ext.text import Text as ExtText
from stacks.metadata.models import Text


pytestmark = pytest.mark.usefixtures('db')


def test_ingest(ext_corpus):

    """
    Text.ingest() should load texts from the ENV-defined corpus.
    """

    now = dt.now()

    t1 = ExtText(dict(
        corpus='corpus1',
        identifier='identifier1',
        title='title1',
        plain_text='text1',
        author_full='last1, first1',
        author_first='first1',
        author_last='last1',
        year=1901,
    ))

    t2 = ExtText(dict(
        corpus='corpus2',
        identifier='identifier2',
        title='title2',
        plain_text='text2',
        author_full='last2, first2',
        author_first='first2',
        author_last='last2',
        year=1902,
    ))

    t3 = ExtText(dict(
        corpus='corpus3',
        identifier='identifier3',
        title='title3',
        plain_text='text3',
        author_full='last3, first3',
        author_first='first3',
        author_last='last3',
        year=1903,
    ))

    ext_corpus.insert_text(t1)
    ext_corpus.insert_text(t2)
    ext_corpus.insert_text(t3)

    Text.ingest()

    assert Text.query.count() == 3

    for text in [t1, t2, t3]:

        # Load the database row.
        row = Text.get_by(
            corpus=text.corpus,
            identifier=text.identifier,
        )

        # Get shared keys.
        keys = text.to_native('metadata').keys()

        # Row should mirror JSON.
        for key in keys:
            assert getattr(row, key) == getattr(text, key)
