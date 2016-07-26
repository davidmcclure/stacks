

from stacks.corpus.models import Text
from stacks.common.singletons import session

from .source import Source


def ingest(corpus_id, path):

    """
    Ingest a CH fiction source XML.

    Args:
        corpus_id (int)
        path (str)
    """

    source = Source(path)

    for text in source.texts():

        Text.create(
            corpus_id=corpus_id,
            identifier=text.identifier(),
            title=text.title(),
            author_name_full=text.author_name_full(),
            year=text.year(),
            plain_text=text.plain_text(),
        )

    session.commit()
