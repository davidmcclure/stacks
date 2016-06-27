

from django.core.management.base import BaseCommand

from corpus.adapters.litlab_c20.corpus import Corpus



class Command(BaseCommand):


    help = 'Ingest Literary Lab 20th Century.'


    def handle(self, *args, **kwargs):
        Corpus.from_env().ingest()
