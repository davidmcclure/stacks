

from corpus.models import Text

from .source import Source


def ingest(corpus_id, path):

    """
    Ingest a Chadwyck Healey source XML.

    Args:
        corpus_id (int)
        path (str)
    """

    source = Source(path)

    for text in source.texts():

        row = Text(
            corpus_id=corpus_id,
            identifier=text.identifier(),
            title=text.title(),
            author_name_full=text.author_name_full(),
            year=text.year(),
            plain_text=text.plain_text(),
        )

        row.full_clean()

        row.save()
