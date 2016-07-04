

from corpus.models import Text as StacksText

from .text import Text


def ingest(corpus_id, path):

    """
    Ingest an ECCO text.

    Args:
        path (str)
    """

    text = Text(path)

    row = StacksText(
        corpus_id=corpus_id,
        identifier=text.identifier(),
        title=text.title(),
        author_name_full=text.author_marc_name(),
        year=text.year(),
        plain_text=text.plain_text(),
    )

    row.full_clean()

    row.save()
