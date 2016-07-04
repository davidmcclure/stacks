

from corpus.models import Text as StacksText

from .text import Text


def ingest(corpus_id, path):

    """
    Ingest a NCCO text.

    Args:
        corpus_id (int)
        path (str)
    """

    text = Text(path)

    row = StacksText(
        corpus_id=corpus_id,
        identifier=text.identifier(),
        plain_text=text.plain_text(),
        title=text.title(),
        year=text.year(),
    )

    row.full_clean()

    row.save()
