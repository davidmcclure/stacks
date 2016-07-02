

from django.core.management.base import BaseCommand

from corpus.adapters.chicago.corpus import Corpus


class Command(BaseCommand):

    help = 'Chicago Corpus'

    def handle(self, *args, **kwargs):
        Corpus.from_env().ingest()
