

from schematics.models import Model
from schematics.types import StringType, IntType

from stacks.adapters.gail_amfic import Text as GailAmficText
from stacks.adapters.ecco import Text as ECCOText


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
