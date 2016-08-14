

from datetime import datetime as dt

from schematics.models import Model
from schematics.types import StringType, IntType, DateTimeType

from stacks.utils import git_rev
from .schema_types import MetadataType


class Text(Model):

    version = StringType(default=git_rev(), required=True)

    created_at = DateTimeType(default=dt.now, required=True)

    corpus = StringType(required=True)

    identifier = StringType(required=True)

    title = StringType(required=True)

    plain_text = StringType(required=True)

    author_full = MetadataType()

    author_first = MetadataType()

    author_last = MetadataType()

    year = IntType()
