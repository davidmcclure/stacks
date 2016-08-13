

from schematics.models import Model
from schematics.types import StringType

from .types import MetadataType


class Name(Model):

    full = MetadataType()

    first = MetadataType()

    last = MetadataType()
