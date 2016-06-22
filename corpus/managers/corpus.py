

import django_rq

from django.db import models


class CorpusManager(models.Manager):


    def queue_ingest(self, slug, name, paths, job):

        """
        Initialize a corpus, queue ingest jobs.

        Args:
            slug (str)
            name (str)
            paths (iter)
            job (func)
        """

        # Delete existing corpus.
        self.filter(slug=slug).delete()

        # Create a new corpus.
        corpus = self.create(slug=slug, name=name)

        queue = django_rq.get_queue()

        # Spool a job for each source.
        for path in paths:
            queue.enqueue(job, corpus.id, path)
