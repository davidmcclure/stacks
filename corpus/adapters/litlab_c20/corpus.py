

from corpus.models import Corpus as StacksCorpus
from corpus.adapters.litlab.corpus import Corpus as LitLabCorpus
from corpus.adapters.litlab.jobs import ingest


class Corpus(LitLabCorpus):


    @classmethod
    def from_env(cls):

        """
        Wrap the ENV-defined root.

        Returns: cls
        """

        return cls(settings.CORPUS_LITLAB_C20)


    def ingest(self):

        """
        Queue ingest jobs for each text.
        """

        StacksCorpus.objects.queue_ingest(
            slug='litlab-c20',
            name='Literary Lab 20th Century Corpus',
            paths=self.text_paths(),
            job=ingest,
        )
