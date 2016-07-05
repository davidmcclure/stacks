

import uuid
import os
import json

from datetime import datetime as dt

from corpus.models import Text
from corpus.utils import git_head_sha


class BundleWriter:

    def __init__(self, data_path, filters):

        """
        Set the data path and filters, create a bundle identifier.

        Args:
            data_path (str)
            filters (dict)
        """

        self.data_path = data_path

        self.filters = filters

        self.slug = str(uuid.uuid4())

    def directory_path(self):

        """
        Returns: str
        """

        return os.path.join(self.data_path, self.slug)

    def metadata_path(self):

        """
        Returns: str
        """

        return os.path.join(self.directory_path(), 'metadata.json')

    def create_directory(self):

        """
        Stub out the bundle folder.
        """

        path = self.directory_path()

        if not os.path.exists(path):
            os.makedirs(path)

    def write_metadata(self):

        """
        Write the metadata.json file.
        """

        metadata = dict(
            created=dt.now().isoformat(),
            stacks_version=git_head_sha(),
            filters=self.filters,
        )

        with open(self.metadata_path(), 'w') as fh:
            json.dump(metadata, fh, indent=2)
