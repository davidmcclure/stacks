

from datetime import datetime as dt

from schematics.models import Model
from schematics.types import StringType, IntType, DateTimeType

from stacks.adapters.bpo import Article as BPOArticle
from stacks.adapters.gail_amfic import Text as GailAmficText
from stacks.adapters.ecco import Text as ECCOText
from stacks.adapters.chadh_drama import Source as CHADHDramaSource
from stacks.adapters.chadh_fiction import Source as CHADHFictionSource
from stacks.adapters.chadh_poetry import Source as CHADHPoetrySource
from stacks.adapters.chicago import Novel as ChicagoNovel
from stacks.adapters.dime_westerns import Text as DimeWesternsText
from stacks.adapters.eebo import Text as EEBOText
from stacks.adapters.litlab import Text as LitLabText

from stacks.singletons import version
from .types import MetadataType


class Text(Model):


    version = StringType(default=version)

    created_at = DateTimeType(default=dt.now)

    corpus = StringType(required=True)

    identifier = StringType(required=True)

    title = StringType(required=True)

    plain_text = StringType(required=True)

    author_name_full = MetadataType()

    author_name_first = MetadataType()

    author_name_last = MetadataType()

    year = IntType()


    @classmethod
    def from_gail_amfic(cls, path):

        """
        Gail American Fiction

        Args:
            path (str)
        """

        text = GailAmficText(path)

        return cls(dict(

            # TODO: ENV-ify corpus name?
            corpus = 'gail-amfic',
            identifier = text.identifier(),
            title = text.title(),
            plain_text = text.plain_text(),

            author_name_full = text.author_name_full(),
            author_name_first = text.author_name_first(),
            author_name_last = text.author_name_last(),

            year = text.year(),

        ))

    @classmethod
    def from_ecco(cls, path):

        """
        ECCO

        Args:
            path (str)
        """

        text = ECCOText(path)

        return cls(dict(

            corpus = 'ecco',
            identifier = text.identifier(),
            title = text.title(),
            plain_text = text.plain_text(),

            author_name_full = text.author_marc_name(),

            year = text.year(),

        ))

    @classmethod
    def from_bpo(cls, *args, **kwargs):

        """
        BPO

        Args:
            zipfile_path (str)
            xml_name (str)
        """

        article = BPOArticle(*args, **kwargs)

        return cls(dict(

            corpus = 'bpo',
            identifier = article.identifier(),
            title = article.title(),
            plain_text = article.plain_text(),

            author_name_full = article.author_name_full(),
            author_name_first = article.author_name_first(),
            author_name_last = article.author_name_last(),

            year = article.year(),

        ))

    @classmethod
    def from_chadh_drama(cls, path):

        """
        Chadwyck Healey Drama

        Args:
            path (str)
        """

        source = CHADHDramaSource(path)

        for play in source.plays():

            yield cls(dict(

                corpus = 'chadh-drama',
                identifier = play.identifier(),
                title = play.title(),
                plain_text = play.plain_text(),

                author_name_full = play.author_name_full(),

                year = play.year(),

            ))

    @classmethod
    def from_chadh_fiction(cls, path):

        """
        Chadwyck Healey Fiction

        Args:
            path (str)
        """

        source = CHADHFictionSource(path)

        for text in source.texts():

            yield cls(dict(

                corpus = 'chadh-fiction',
                identifier = text.identifier(),
                title = text.title(),
                plain_text = text.plain_text(),

                author_name_full = text.author_name_full(),

                year = text.year(),

            ))

    @classmethod
    def from_chadh_poetry(cls, path):

        """
        Chadwyck Healey Poetry

        Args:
            path (str)
        """

        source = CHADHPoetrySource(path)

        for poem in source.poems():

            yield cls(dict(

                corpus = 'chadh-poetry',
                identifier = poem.identifier(),
                title = poem.title(),
                plain_text = poem.plain_text(),

                author_name_full = poem.author_name_full(),

                year = poem.year(),

            ))

    @classmethod
    def from_chicago(cls, *args, **kwargs):

        """
        Chicago

        Args:
            corpus_path (str)
            metadata (dict)
        """

        novel = ChicagoNovel(*args, **kwargs)

        return cls(dict(

            corpus = 'chicago',
            identifier = novel.identifier(),
            title = novel.title(),
            plain_text = novel.source_text(),

            author_name_full = novel.author_name_full(),
            author_name_first = novel.author_name_first(),
            author_name_last = novel.author_name_last(),

            year = novel.year(),

        ))

    @classmethod
    def from_dime_westerns(cls, *args, **kwargs):

        """
        Dime Westerns

        Args:
            texts_path (str)
            slug (str)
            metadata (dict)
        """

        text = DimeWesternsText(*args, **kwargs)

        return cls(dict(

            corpus = 'dime-westerns',
            identifier = text.identifier(),
            title = text.title(),
            plain_text = text.source_text(),

            author_name_full = text.author_name_full(),

            year = text.year(),

        ))

    @classmethod
    def from_eebo(cls, path):

        """
        EEBO

        Args:
            path (str)
        """

        text = EEBOText(path)

        return cls(dict(

            corpus = 'eebo',
            identifier = text.identifier(),
            title = text.title(),
            plain_text = text.plain_text(),

            author_name_full = text.author(),

            year = text.year(),

        ))

    @classmethod
    def from_litlab_c20(cls, path):

        """
        Literary Lab 20th Century

        Args:
            path (str)
        """

        text = LitLabText(path)

        return cls(dict(

            corpus = 'litlab-c20',
            identifier = text.identifier(),
            title = text.title(),
            plain_text = text.source_text(),

            author_name_full = text.author.folder_name(),
            author_name_first = text.author.name_first(),
            author_name_last = text.author.name_last(),

            year = text.year(),

        ))

    @classmethod
    def from_litlab_suspense(cls, path):

        """
        Literary Lab Suspense

        Args:
            path (str)
        """

        text = LitLabText(path)

        return cls(dict(

            corpus = 'litlab-suspense',
            identifier = text.identifier(),
            title = text.title(),
            plain_text = text.source_text(),

            author_name_full = text.author.folder_name(),
            author_name_first = text.author.name_first(),
            author_name_last = text.author.name_last(),

            year = text.year(),

        ))
