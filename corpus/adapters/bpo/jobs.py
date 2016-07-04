

from corpus.models import Text as StacksText

from .article import Article


def ingest(corpus_id, zipfile_path, xml_name):

    """
    Ingest a BPO article.

    Args:
        zipfile_path (str)
        xml_name (str)
    """

    article = Article(zipfile_path, xml_name)

    row = StacksText(
        corpus_id=corpus_id,
        identifier=article.identifier(),
        plain_text=article.plain_text(),
        title=article.title(),
        author_name_full=article.author_name_full(),
        author_name_first=article.author_name_first(),
        author_name_last=article.author_name_last(),
        year=article.year(),
    )

    row.full_clean()

    row.save()
