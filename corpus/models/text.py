

from django.db import models


class Text(models.Model):

    corpus = models.ForeignKey('Corpus')

    # The original representation of the text.
    source_text = models.TextField()

    # Plain text extracted from the source markup.
    plain_text = models.TextField()

    # Metadata:

    title = models.TextField()

    author = models.TextField(
        null=True
    )

    year = models.IntegerField(
        null=True
    )
