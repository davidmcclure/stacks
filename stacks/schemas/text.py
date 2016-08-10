

from schematics.models import Model
from schematics.types import StringType, IntType


class Text(Model):


    corpus = StringType(required=True)

    identifier = StringType(required=True)

    title = StringType(required=True)

    plain_text = StringType(required=True)

    author_name_full = StringType()

    author_name_first = StringType()

    author_name_last = StringType()

    year = IntType()
