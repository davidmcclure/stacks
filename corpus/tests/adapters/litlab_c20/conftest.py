

import pytest

from .mock_litlab_c20 import MockLitLabC20


@pytest.yield_fixture
def mock_corpus():

    """
    Provide a mock corpus instance.

    Yields: MockLitLabC20
    """

    corpus = MockLitLabC20()

    yield corpus

    corpus.teardown()
