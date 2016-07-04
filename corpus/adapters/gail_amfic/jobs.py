

from corpus.models import Text as StacksText

from .text import Text


def ingest(corpus_id, path):

    """
    Ingest a Gail American Fiction text.

    Args:
        path (str)
    """

    text = Text(path)

    row = StacksText(
        corpus_id=corpus_id,
        identifier=text.identifier(),
        title=text.title(),
        author_name_full=text.author_name_full(),
        author_name_first=text.author_name_first(),
        author_name_last=text.author_name_last(),
        year=text.year(),
        plain_text=text.plain_text(),
    )

    row.full_clean()

    row.save()
