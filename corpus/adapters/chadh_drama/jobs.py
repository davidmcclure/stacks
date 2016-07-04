

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

    for play in source.plays():

        text = Text(
            corpus_id=corpus_id,
            identifier=play.identifier(),
            title=play.title(),
            author_name_full=play.author_name_full(),
            year=play.year(),
            plain_text=play.plain_text(),
        )

        text.full_clean()

        text.save()
