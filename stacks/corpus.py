

import attr
import os
import pickle
import bz2
import uuid

from cityhash import CityHash32
from boltons.iterutils import chunked_iter

from stacks import session, config
from stacks.utils import scan_paths


@attr.s
class Corpus:

    path = attr.ib()

    @classmethod
    def from_env(cls):
        """Wrap the ENV-defined root.

        Returns: cls
        """
        return cls(config['data']['ext'])

    def index_rows(self, corpus, source, rows):
        """Dump db rows + (annotated) text.

        Args:
            corpus (str): A slug for the corpus.
            source (str): An identifier for the source entity.
            rows (list of model instances)
        """
        for row in rows:
            if getattr(row, '_text', None):
                self.write_text(row)

        self.pickle_rows(corpus, source, rows)

    def pickle_rows(self, corpus, source, rows):
        """Pickle row instances.

        Args:
            corpus (str): A slug for the corpus.
            source (str): An identifier for the source entity.
            rows (list of model instances)
        """
        # Form the hash directories.
        source_hash = str(CityHash32(source))
        prefix = source_hash[:3]
        suffix = source_hash[3:]

        # Form the row path.
        row_name = '{}.p'.format(suffix)
        row_path = os.path.join(self.path, 'rows', corpus, prefix, row_name)

        # Create the directory.
        os.makedirs(os.path.dirname(row_path), exist_ok=True)

        with open(row_path, 'wb') as fh:
            pickle.dump(rows, fh)

    def write_text(self, row):
        """Write plain text + annotations.
        """
        prefix = row.text_hash[:3]
        suffix = row.text_hash[3:]

        # Form the file path.
        text_path = os.path.join(
            self.path, 'texts', row.corpus,
            prefix, suffix, 'text.bz2',
        )

        # Create the text directory.
        os.makedirs(os.path.dirname(text_path), exist_ok=True)

        with bz2.open(text_path, 'wt') as fh:
            print(row._text, file=fh)

        # TODO: annotations

    def db_rows(self):
        """Generate database rows.
        """
        for path in scan_paths(self.path, '\.p'):
            with open(path, 'rb') as fh:
                yield from pickle.load(fh)

    def load_db(self, chunk_size=1000):
        """Write db rows.
        """
        for chunk in chunked_iter(self.db_rows(), chunk_size):
            session.bulk_save_objects(chunk)
            session.flush()

        session.commit()

    def load_text(self, row):
        """Given a metadata row, hydrate plain text.

        Args:
            row (Text)

        Returns: str
        """
        prefix = row.text_hash[:3]
        suffix = row.text_hash[3:]

        # Form the file path.
        text_path = os.path.join(
            self.path, 'texts', row.corpus,
            prefix, suffix, 'text.bz2',
        )

        with bz2.open(text_path) as fh:
            return str(fh.read())
