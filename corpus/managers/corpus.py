

import django_rq

from django.db import models


class CorpusManager(models.Manager):

    def queue_ingest(self, slug, name, args, job):

        """
        Reset a corpus and queue text ingest jobs in RQ.

        Args:
            slug (str)
            name (str)
            args (iter)
            job (func)
        """

        # Delete existing corpus.
        self.filter(slug=slug).delete()

        # Create a new corpus.
        corpus = self.create(slug=slug, name=name)

        queue = django_rq.get_queue()

        # Spool a job for each source.
        for arg in args:

            if type(arg) is dict:
                queue.enqueue(job, corpus.id, **arg)

            else:
                queue.enqueue(job, corpus.id, arg)
