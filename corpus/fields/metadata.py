

from django.db import models


class MetadataField(models.TextField):

    def clean(self, value, model_instance):

        """
        Strip metadata values.
        """

        if value:
            value = value.strip()

        return super().clean(value, model_instance)
