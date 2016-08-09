

from stacks.singletons import session
from stacks.models import Text as StacksText

from .text import Text


def ingest(corpus_id, texts_path, slug, metadata):

    """
    Ingest a Dime Western.

    Args:
        corpus_id (int)
        texts_path (str)
        slug (str)
        metadata (dict)
    """

    text = Text(texts_path, slug, metadata)

    StacksText.create(
        corpus_id=corpus_id,
        identifier=text.identifier(),
        title=text.title(),
        author_name_full=text.author_name_full(),
        year=text.year(),
        plain_text=text.source_text(),
    )

    session.commit()
