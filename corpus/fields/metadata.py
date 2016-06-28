

from django.db import models


class MetadataField(models.TextField):

    def clean(self, value, model_instance):

        """
        Strip metadata values.
        """

        cleaned = value.strip()

        return super().clean(cleaned, model_instance)
