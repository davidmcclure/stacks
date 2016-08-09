

import os

from zipfile import ZipFile

from stacks.utils import scan_paths
from stacks.models import Corpus as StacksCorpus
from stacks.singletons import session

from .jobs import ingest


class Corpus:

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

        return scan_paths(self.path, '\.zip$')

    def xml_paths(self):

        """
        Get (archive, path) tuples for each of the compressed XML sources.

        Yields: (str, str)
        """

        # Walk .zip files.
        for zpath in self.zip_paths():
            with ZipFile(zpath) as archive:

                # Walk zipped XML files.
                for name in archive.namelist():
                    yield (zpath, name)

    def ingest(self):

        """
        Queue ingest jobs for each zip + xml.
        """

        corpus = StacksCorpus.replace(
            slug='bpo',
            name='British Periodicals Online',
        )

        session.commit()

        corpus.queue_ingest(ingest, [
            dict(zipfile_path=zpath, xml_name=name)
            for zpath, name in self.xml_paths()
        ])
