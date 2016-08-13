

from schematics.models import Model
from schematics.types.compound import ModelType

from .name import Name


class Author(Model):

    name = ModelType(Name, default=dict, required=True)
