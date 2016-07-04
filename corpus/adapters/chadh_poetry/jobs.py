

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

    for poem in source.poems():

        text = Text(
            corpus_id=corpus_id,
            identifier=poem.identifier(),
            title=poem.title(),
            author_name_full=poem.author_name_full(),
            year=poem.year(),
            plain_text=poem.plain_text(),
        )

        text.full_clean()

        text.save()
