

from datetime import datetime as dt

from schematics.models import Model
from schematics.types import StringType, IntType, DateTimeType

from stacks.singletons import version


class MetadataType(StringType):

    def to_native(self, *args, **kwargs):

        """
        Strip incoming values.
        """

        val = super().to_native(*args, **kwargs)

        return val.strip()


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
