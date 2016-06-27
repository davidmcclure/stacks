

from django.core.management.base import BaseCommand

from corpus.adapters.litlab_suspense.corpus import Corpus



class Command(BaseCommand):


    help = 'Literary Lab Suspense Corpus'


    def handle(self, *args, **kwargs):
        Corpus.from_env().ingest()
