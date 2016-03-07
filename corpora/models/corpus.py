

from django.db import models


class Corpus(models.Model):


    class Meta:
        verbose_name_plural = 'corpora'


    name = models.CharField(
        max_length=200,
    )


    def __str__(self):
        return self.name


    @classmethod
    def ingest(cls, adapter):

        """
        Ingest a corpus.

        Args:
            adapter (stacks.corpora.Adapter)
        """

        pass
