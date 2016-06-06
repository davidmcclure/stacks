

from django.db import models


class Text(models.Model):


    corpus = models.ForeignKey('Corpus')

    identifier = models.CharField(
        db_index=True,
        max_length=100,
    )

    # ** Content

    source_text = models.TextField()

    plain_text = models.TextField()


    # ** Metadata

    title = models.TextField()

    author = models.TextField(
        null=True,
    )

    year = models.IntegerField(
        null=True,
    )


    class Meta:
        unique_together = ('corpus', 'identifier')
