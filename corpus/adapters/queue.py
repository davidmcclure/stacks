

import django_rq

from corpus.models import Corpus, Text


class QueueAdapter:


    @property
    def name(self):

        """
        A human-readable name for the corpus.
        """

        raise NotImplementedError


    @property
    def slug(self):

        """
        A unique slug for the corpus (for URLs, etc).
        """

        raise NotImplementedError


    @classmethod
    def from_env(cls):

        """
        Make an instance from the ENV-defined corpus path.
        """

        raise NotImplementedError


    @classmethod
    def job(self, corpus_id, path):

        """
        Given a corpus id and a resource path, insert a new text.

        Args:
            corpus_id (int): The id of the parent corpus.
            path (str): The filesystem path of the resource.
        """

        raise NotImplementedError


    def paths(self):

        """
        A stream of paths for individual resources in the corpus.
        """

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
        for path in self.paths():
            queue.enqueue(self.__class__.job, corpus.id, path)
