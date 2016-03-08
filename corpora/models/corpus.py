

from django.db import models

from corpora import fields


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

        # delete existing corpus
        # create new corpus
        # iterate over the adapter
        # merge in the corpus reference
        # insert the text

        # Delete the existing corpus.
        cls.objects.filter(slug=adapter.slug).delete()

        # Create a new corpus.
        corpus = cls.objects.create(slug=adapter.slug)

        for row in adapter:
            pass
