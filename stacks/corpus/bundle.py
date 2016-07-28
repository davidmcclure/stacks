

import os


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
        return os.path.join(self.bundle_path, 'manifest.json')

    def add_text(self, text):

        """
        Add a text to the corpus.
        """

        # construct the file path (checksum)
        # create the directories
        # write the text as a JSON blob

        pass

    def add_metadata(self):
        pass

    def write_manifest(self):
        pass

    def compress(self):
        pass
