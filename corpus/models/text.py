

from django.db import models

from corpus import fields


class Text(models.Model):


    class Meta:
        unique_together = ('corpus', 'identifier')


    corpus = models.ForeignKey('Corpus')

    identifier = models.CharField(
        db_index=True,
        max_length=100,
    )


    # Content
    # -------

    plain_text = models.TextField()


    # Metadata
    # --------

    title = fields.MetadataField()

    author_name_full = fields.MetadataField(
        null=True,
        blank=True,
    )

    author_name_first = fields.MetadataField(
        null=True,
        blank=True,
    )

    author_name_last = fields.MetadataField(
        null=True,
        blank=True,
    )

    year = models.IntegerField(
        null=True,
        blank=True,
    )
