

from django.db import models


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

    source_text = models.TextField()

    plain_text = models.TextField()


    # Metadata
    # --------

    title = models.TextField()

    author_name_full = models.TextField(
        null=True,
    )

    author_name_first = models.TextField(
        null=True,
    )

    author_name_last = models.TextField(
        null=True,
    )

    year = models.IntegerField(
        null=True,
    )
