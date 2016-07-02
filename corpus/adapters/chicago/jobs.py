

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

    row = StacksText(
        corpus_id=corpus_id,
        identifier=novel.identifier(),
        plain_text=novel.source_text(),
        title=novel.title(),
        author_name_full=novel.author_name_full(),
        author_name_first=novel.author_name_first(),
        author_name_last=novel.author_name_last(),
        year=novel.year(),
    )

    row.full_clean()

    row.save()
