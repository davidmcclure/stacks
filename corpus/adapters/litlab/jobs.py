

from corpus.models import Text as StacksText

from .text import Text


def ingest(corpus_id, path):

    """
    Ingest a C20 text.

    Args:
        corpus_id (int)
        path (str)
    """

    text = Text(path)

    row = StacksText(
        corpus_id=corpus_id,
        identifier=text.identifier(),
        title=text.title(),
        author_name_full=text.author.folder_name(),
        author_name_first=text.author.name_first(),
        author_name_last=text.author.name_last(),
        year=text.year(),
        plain_text=text.source_text(),
    )

    row.full_clean()

    row.save()
