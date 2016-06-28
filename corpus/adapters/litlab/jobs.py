

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
        corpus_id=corpus_id,
        identifier=text.identifier(),
        source_text=text.source_text(),
        title=text.title(),
        author_name_full=text.author.folder_name(),
        author_name_first=text.author.name_first(),
        author_name_last=text.author.name_last(),
        year=text.year(),
    )
