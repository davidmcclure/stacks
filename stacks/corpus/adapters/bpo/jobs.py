

from stacks.corpus.models import Text
from stacks.common.utils import with_commit

from .article import Article


@with_commit
def ingest(corpus_id, zipfile_path, xml_name):

    """
    Ingest a BPO article.
    """

    article = Article(zipfile_path, xml_name)

    Text.create(
        corpus_id=corpus_id,
        identifier=article.identifier(),
        title=article.title(),
        author_name_full=article.author_name_full(),
        author_name_first=article.author_name_first(),
        author_name_last=article.author_name_last(),
        year=article.year(),
        plain_text=article.plain_text(),
    )
