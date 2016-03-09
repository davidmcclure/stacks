

import sys

from django.db import models

from corpora import fields
from corpora.models import Text


class Corpus(models.Model):


    class Meta:
        verbose_name_plural = 'corpora'


    name = models.CharField(
        max_length=200,
    )

    slug = fields.SlugField(
        max_length=200,
    )


    def __str__(self):
        return self.name


    @classmethod
    def ingest(cls, adapter):

        """
        Ingest a corpus.

        Args:
            adapter (Adapter)
        """

        # Delete the existing corpus.
        cls.objects.filter(slug=adapter.slug).delete()

        # Create a new corpus.
        corpus = cls.objects.create(
            name=adapter.name,
            slug=adapter.slug,
        )

        for i, row in enumerate(adapter):

            # Insert the text.
            row.update(dict(corpus=corpus))
            Text.objects.create(**row)

            sys.stdout.write('\r'+str(i))
            sys.stdout.flush()
