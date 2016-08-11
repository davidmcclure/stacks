

from schematics.types import StringType


class MetadataType(StringType):

    def to_native(self, *args, **kwargs):

        """
        Strip incoming values.
        """

        val = super().to_native(*args, **kwargs)

        return val.strip()
