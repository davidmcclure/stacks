

from django.core.management.base import BaseCommand
from pydoc import locate


class Command(BaseCommand):


    help = 'Queue ingest jobs for a corpus.'


    def add_arguments(self, parser):
        parser.add_argument('corpus', type=str)


    def handle(self, corpus, **kwargs):

        """
        Import the requested corpus adapter, queue jobs.
        """

        Corpus = locate('corpus.adapters.{0}'.format(corpus))
        Corpus.from_env().queue()
