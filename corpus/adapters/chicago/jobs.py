

from corpus.models import Text as StacksText

from .novel import Novel


def ingest(corpus_id, metadata):
    """
    Ingest a Chicago novel.

    Args:
        corpus_id (int)
        metadata (dict)
    """
    novel = Novel.from_env(metadata)

    StacksText.objects.create(
        corpus_id=corpus_id,
        identifier=novel.identifier(),
        plain_text=novel.plain_text(),
        title=novel.title(),
        author=novel.author(),
        year=novel.year(),
    )
