

import os
import json

from stacks.common.utils import open_makedirs
from stacks.corpus.utils import scan_paths


class Bundle:

    def __init__(self, data_path, name):

        """
        Set the bundle name.

        Args:
            data_path (str)
            name (str)
        """

        self.data_path = os.path.abspath(data_path)

        self.name = name

    @property
    def bundle_path(self):
        return os.path.join(self.data_path, self.name)

    @property
    def compressed_bundle_path(self):
        return self.bundle_path + '.tar.gz'

    @property
    def texts_path(self):
        return os.path.join(self.bundle_path, 'texts')

    @property
    def metadata_path(self):
        return os.path.join(self.bundle_path, 'metadata.json')

    @property
    def manifest_path(self):
        return os.path.join(self.bundle_path, 'manifest.txt')

    def write_text(self, text):

        """
        Add a text to the corpus.

        Args:
            text (corpus.Text)
        """

        checksum = text.checksum()

        path = os.path.join(
            self.texts_path,
            checksum[:3],
            checksum[3:]+'.json',
        )

        with open_makedirs(path, 'w') as fh:
            json.dump(text.asdict(), fh, indent=2)

    def write_metadata(self, metadata):

        """
        Write the metadata.json content.

        Args:
            metadata (dict)
        """

        with open_makedirs(self.metadata_path, 'w') as fh:
            json.dump(metadata, fh, indent=2)

    def write_manifest(self):

        """
        Write relative text paths to manifest.txt.
        """

        with open_makedirs(self.manifest_path, 'w') as fh:

            # Scan JSON files.
            for path in scan_paths(self.texts_path, '\.json$'):

                # Write path relative to bundle root.
                relpath = os.path.relpath(path, self.bundle_path)
                print(relpath, file=fh)

    def compress(self):
        pass
