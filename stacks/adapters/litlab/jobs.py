

from stacks.singletons import session
from stacks.models import Text as StacksText

from .text import Text


def ingest(corpus_id, path):

    """
    Ingest a Lit Lab text.

    Args:
        corpus_id (int)
        path (str)
    """

    text = Text(path)

    StacksText.create(
        corpus_id=corpus_id,
        identifier=text.identifier(),
        title=text.title(),
        author_name_full=text.author.folder_name(),
        author_name_first=text.author.name_first(),
        author_name_last=text.author.name_last(),
        year=text.year(),
        plain_text=text.source_text(),
    )

    session.commit()
