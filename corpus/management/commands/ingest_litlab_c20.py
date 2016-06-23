

from django.core.management.base import BaseCommand

from corpus.adapters.litlab_c20.corpus import Corpus


class Command(BaseCommand):


    help = 'Ingest the Literary Lab 20th century corpus.'


    def handle(self, *args, **kwargs):
        Corpus.from_env().ingest()
