

from datetime import datetime as dt

from schematics.types import StringType, IntType, DateTimeType
from schematics.models import Model

from stacks.schema_types import MetadataType
from stacks.singletons import version


class JSONText(Model):

    version = StringType(default=version, required=True)

    created_at = DateTimeType(default=dt.now, required=True)

    corpus = StringType(required=True)

    identifier = StringType(required=True)

    title = StringType(required=True)

    plain_text = StringType(required=True)

    author_name_full = MetadataType()

    author_name_first = MetadataType()

    author_name_last = MetadataType()

    year = IntType()
