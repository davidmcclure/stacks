

import os

from stacks.common.singletons import config, session
from stacks.corpus.models import Export, Text


class Exporter:

    def from_env(cls, export):

        """
        Make an exported from the ENV-defined data path.

        Args:
            export (Export)
        """

        return cls(config['export_path'], export)

    def __init__(self, data_path, export):

        """
        Construct the text query.

        Args:
            data_path (str)
            export (Export)
        """

        self.path = os.path.join(data_path, export.uuid)

        # Filter by corpora.
        query = (
            session.query(Text)
            .filter(Text.corpus_id.in_(export.corpora))
        )

        # Filter by year.

        if export.min_year:
            query = query.filter(Text.year >= export.min_year)

        if export.max_year:
            query = query.filter(Text.year <= export.min_year)

        # TODO: Sample size.

        self.query = query

    def texts_path(self):

        """
        Get the /texts path.

        Returns: str
        """

        return os.path.join(self.path, 'texts')

    def __call__(self):

        """
        Generate and package the bundle.
        """

        self._create_directories()

        self._write_texts()

        self._write_metadata()

        self._compress()

    def _create_directories(self):

        """
        Create / and /texts.
        """

        os.makedirs(self.texts_path())
