

from stacks.corpus.models import Text
from stacks.common.utils import with_commit

from .novel import Novel


@with_commit
def ingest(corpus_id, corpus_path, metadata):

    """
    Ingest a Chicago novel.

    Args:
        corpus_id (int)
        corpus_path (str)
        metadata (dict)
    """

    novel = Novel(corpus_path, metadata)

    Text.create(
        corpus_id=corpus_id,
        identifier=novel.identifier(),
        title=novel.title(),
        author_name_full=novel.author_name_full(),
        author_name_first=novel.author_name_first(),
        author_name_last=novel.author_name_last(),
        year=novel.year(),
        plain_text=novel.source_text(),
    )
