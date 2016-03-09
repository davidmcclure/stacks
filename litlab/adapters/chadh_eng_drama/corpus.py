

import glob
import os

from litlab.conf import settings

from corpora.models import Text as PGText, Corpus as PGCorpus
from .text import Text


class Corpus:


    name = 'Chadwyck Healey English Drama'

    slug = 'chadwyck-healey-english-drama'


    @classmethod
    def from_env(cls):

        """
        Wrap the settings-defined path.
        """

        return cls(settings.LITLAB_CHADH_ENGLISH_DRAMA)


    @classmethod
    def insert_text(cls, corpus_id, path):

        """
        Add an individual text.

        Args:
            corpus_id (int): The id of the parent corpus.
            path (str): The path of the XML file.
        """

        text = Text(path)

        # Build the text params.
        row = text.build_row(corpus_id)

        # Write the new text.
        PGText.objects.create(**row)

        print(path)


    def __init__(self, path):

        """
        Set the corpus path.

        Args:
            path (str): The corpus path.
        """

        self.path = os.path.abspath(path)


    def paths(self):

        """
        Generate text paths.

        Yields:
            str: The next path
        """

        for path in glob.glob(os.path.join(self.path, '*.new')):
            yield path


    def queue(self):

        """
        Queue accessioning jobs.
        """

        # Delete the existing corpus.
        PGCorpus.objects.filter(slug=self.slug).delete()

        # Create a new corpus.
        corpus = PGCorpus.objects.create(
            name=self.name,
            slug=self.slug,
        )

        # TODO|dev
        for path in self.paths():
            self.__class__.insert_text(corpus.id, path)
