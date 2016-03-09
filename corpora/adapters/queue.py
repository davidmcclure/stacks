

import django_rq

from corpora.models import Corpus, Text


class QueueAdapter:


    @property
    def name(self):
        raise NotImplementedError


    @property
    def slug(self):
        raise NotImplementedError


    @property
    def paths(self):
        raise NotImplementedError


    @classmethod
    def job(self, corpus_id, path):
        raise NotImplementedError


    def queue(self):

        """
        Queue accessioning jobs in RQ.
        """

        # Delete the existing corpus.
        Corpus.objects.filter(slug=self.slug).delete()

        # Create a new corpus.
        corpus = Corpus.objects.create(
            name=self.name,
            slug=self.slug,
        )

        queue = django_rq.get_queue()

        # Spool a job for each source.
        for path in self.paths:
            queue.enqueue(self.__class__.job, corpus.id, path)
