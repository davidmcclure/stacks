

from stacks.corpus.models import Text as StacksText

from .text import Text


def ingest(corpus_id, path):

    """
    Ingest an EEBO text.

    Args:
        path (str)
    """

    text = Text(path)

    StacksText.create(
        corpus_id=corpus_id,
        identifier=text.identifier(),
        title=text.title(),
        author_name_full=text.author(),
        year=text.year(),
        plain_text=text.plain_text(),
    )
