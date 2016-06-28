

from corpus.models import Text as StacksText

from .novel import Novel


def ingest(corpus_id, corpus_path, metadata):

    """
    Ingest a Chicago novel.

    Args:
        corpus_id (int)
        metadata (dict)
    """

    novel = Novel(corpus_path, metadata)

    StacksText.objects.create(
        corpus_id=corpus_id,
        identifier=novel.identifier(),
        plain_text=novel.plain_text(),
        title=novel.title(),
        author=novel.author(),
        year=novel.year(),
    )
