

from schematics.models import Model
from schematics.types import StringType, IntType

from stacks.adapters.bpo import Article as BPOArticle
from stacks.adapters.gail_amfic import Text as GailAmficText
from stacks.adapters.ecco import Text as ECCOText
from stacks.adapters.chadh_drama import Source as CHADHDramaSource
from stacks.adapters.chadh_fiction import Source as CHADHFictionSource


class Text(Model):


    corpus = StringType(required=True)

    identifier = StringType(required=True)

    title = StringType(required=True)

    plain_text = StringType(required=True)

    author_name_full = StringType()

    author_name_first = StringType()

    author_name_last = StringType()

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
    def from_bpo(cls, zipfile_path, xml_name):

        """
        BPO

        Args:
            zipfile_path (str)
            xml_name (str)
        """

        article = BPOArticle(zipfile_path, xml_name)

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
