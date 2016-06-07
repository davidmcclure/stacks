

from django.core.management.base import BaseCommand
from pydoc import locate


class Command(BaseCommand):


    help = 'Queue ingest jobs for a corpus.'


    def add_arguments(self, parser):
        parser.add_argument('corpus', type=str)


    # TODO
    def handle(self, corpus, **kwargs):
        pass
