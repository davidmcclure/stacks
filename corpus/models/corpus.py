

import sys

from django.db import models

from corpus import fields
from corpus.models import Text


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
