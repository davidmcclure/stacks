

from stacks.corpus.models import Text
from stacks.common.utils import with_commit

from .source import Source


@with_commit
def ingest(corpus_id, path):

    """
    Ingest a CH poetry source XML.

    Args:
        corpus_id (int)
        path (str)
    """

    source = Source(path)

    for poem in source.poems():

        Text.create(
            corpus_id=corpus_id,
            identifier=poem.identifier(),
            title=poem.title(),
            author_name_full=poem.author_name_full(),
            year=poem.year(),
            plain_text=poem.plain_text(),
        )
