

import pytest
import os

from corpus.adapters.litlab_c20.author import Author


@pytest.fixture()
def get_author():

    """
    Wrap an author fixture.
    """

    def _get_author(name):

        path = os.path.join(
            os.path.dirname(__file__),
            'fixtures', name,
        )

        return Author(path)

    return _get_author
