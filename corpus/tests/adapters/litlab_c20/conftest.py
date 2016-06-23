

import pytest
import os

from corpus.adapters.litlab_c20.author import Author
from corpus.adapters.litlab_c20.text import Text


@pytest.fixture()
def get_author():

    """
    Wrap an author fixture.
    """

    def _get_author(author_name):

        path = os.path.join(
            os.path.dirname(__file__),
            'fixtures', author_name,
        )

        return Author(path)

    return _get_author


@pytest.fixture()
def get_text():

    """
    Wrap a text fixture.
    """

    def _get_text(author_name, text_name):

        path = os.path.join(
            os.path.dirname(__file__), 'fixtures',
            author_name, text_name,
        )

        return Text(path)

    return _get_text
