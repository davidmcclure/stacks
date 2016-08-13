

from datetime import datetime as dt

from schematics.models import Model
from schematics.types import StringType, DateTimeType, IntType
from schematics.types.compound import ModelType

from stacks.singletons import version

from .author import Author


class Metadata(Model):

    version = StringType(default=version, required=True)

    created_at = DateTimeType(default=dt.now, required=True)

    corpus = StringType(required=True)

    identifier = StringType(required=True)

    title = StringType(required=True)

    author = ModelType(Author, default=dict, required=True)

    year = IntType(required=True)
