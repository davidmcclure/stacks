

import attr
import os
import pickle
import bz2
import uuid


@attr.s
class Corpus:

    path = attr.ib()

    def index_rows(self, corpus, rows):
        """Dump db rows + (annotated) text.

        Args:
            corpus (str): A slug for the corpus.
            rows (list of model instances)
        """
        for row in rows:
            if getattr(row, '_text', None):
                self.write_text(row)

        self.pickle_rows(corpus, rows)

    def pickle_rows(self, corpus, rows):
        """Pickle row instances.
        """
        # Form the row path.
        row_name = '{}.p'.format(str(uuid.uuid4()))
        row_path = os.path.join(self.path, 'rows', corpus, row_name)

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
