

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

    StacksText.objects.create(
        corpus_id = corpus_id,
        plain_text = text.plain_text,
        title = text.title,
        author = text.author.name_full,
        year = text.year,
    )
