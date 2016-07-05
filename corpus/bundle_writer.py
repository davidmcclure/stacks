

import uuid
import os
import json

from datetime import datetime as dt

from django.forms.models import model_to_dict

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

    def query(self):

        """
        Returns: QuerySet
        """

        return Text.objects.filter(**self.filters)

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
            text_count=self.query().count(),
            stacks_version=git_head_sha(),
            filters=self.filters,
        )

        with open(self.metadata_path(), 'w') as fh:
            json.dump(metadata, fh, indent=2)

    def write_texts(self):

        """
        Write the text files.
        """

        for text in self.query():

            checksum = text.checksum()

            segment = checksum[:3]

            # Form the file name.
            file_name = '{0}.json'.format(checksum[3:])

            segment_dir = os.path.join(
                self.directory_path(),
                'texts', segment,
            )

            # Create the segment dir.
            if not os.path.exists(segment_dir):
                os.makedirs(segment_dir)

            path = os.path.join(segment_dir, file_name)

            data = model_to_dict(text)

            # Write the JSON.
            with open(path, 'w') as fh:
                json.dump(data, fh, indent=2)
