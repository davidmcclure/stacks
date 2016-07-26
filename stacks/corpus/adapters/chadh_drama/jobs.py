

from stacks.corpus.models import Text
from stacks.common.singletons import session

from .source import Source


def ingest(corpus_id, path):

    """
    Ingest a CH drama source XML.

    Args:
        corpus_id (int)
        path (str)
    """

    source = Source(path)

    for play in source.plays():

        Text.create(
            corpus_id=corpus_id,
            identifier=play.identifier(),
            title=play.title(),
            author_name_full=play.author_name_full(),
            year=play.year(),
            plain_text=play.plain_text(),
        )

    session.commit()
