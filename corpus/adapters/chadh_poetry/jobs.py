

from corpus.models import Text


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
            # TODO
        )

        text.full_clean()

        text.save()
