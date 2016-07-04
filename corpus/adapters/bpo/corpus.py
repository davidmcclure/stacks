

import os
import scandir

from zipfile import ZipFile

from django.conf import settings

from corpus.models import Corpus as StacksCorpus

from .jobs import ingest


class Corpus:

    @classmethod
    def from_env(cls):

        """
        Wrap the ENV-defined root.
        """

        return cls(settings.CORPUS_BPO)

    def __init__(self, path):

        """
        Canonicalize the corpus path.

        Args:
            path (str)
        """

        self.path = os.path.abspath(path)

    def zip_paths(self):

        """
        Get paths to each of the .zip archives.

        Yields: str
        """

        for root, dirs, files in scandir.walk(self.path):
            for name in files:

                # Match .xml files.
                if os.path.splitext(name)[1] == '.zip':
                    yield os.path.join(root, name)

    def xml_paths(self):

        """
        Get (archive, path) tuples for each of the compressed XML sources.

        Yields: (str, str)
        """

        for zpath in self.zip_paths():
            with ZipFile(zpath) as archive:
                for name in archive.namelist():
                    yield (zpath, name)

    def ingest(self):

        """
        Queue ingest jobs for each text.
        """

        args = [
            dict(zipfile_path=zpath, xml_name=name)
            for zpath, name in self.xml_paths()
        ]

        StacksCorpus.objects.queue_ingest(
            slug='british-periodicals-online',
            name='British Periodicals Online',
            args=args,
            job=ingest,
        )
