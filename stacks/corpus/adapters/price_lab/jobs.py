

from stacks.common.singletons import session
from stacks.corpus.models import Text as StacksText

from .text import Text


def ingest(corpus_id, texts_path, metadata):

    """
    Ingest a Price Lab novel.

    Args:
        corpus_id (int)
        texts_path (str)
        metadata (dict)
    """

    text = Text(texts_path, metadata)

    StacksText.create(
        corpus_id=corpus_id,
        identifier=text.identifier(),
        title=text.title(),
        author_name_full=text.author_name_full(),
        author_name_first=text.author_name_first(),
        author_name_last=text.author_name_last(),
        year=text.year(),
        plain_text=text.source_text(),
    )

    session.commit()
