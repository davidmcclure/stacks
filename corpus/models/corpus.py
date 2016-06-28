

import sys

from django.db import models

from corpus.managers import CorpusManager
from corpus import fields


class Corpus(models.Model):


    objects = CorpusManager()


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
