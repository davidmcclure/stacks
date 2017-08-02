

import os

from sqlalchemy import Column, String
from sqlalchemy.inspection import inspect

from stacks.utils import md5


class Text:

    corpus = Column(String, nullable=False)

    text_hash = Column(String, nullable=False)

    def __init__(self, *args, **kwargs):
        """Set the corpus name, hash PK.
        """
        # Get PK column name.
        pk_col = inspect(self.__class__).primary_key[0].name
        pk_val = kwargs[pk_col]

        # Mirror table name, hash the PK.
        self.corpus = self.__tablename__
        self.text_hash = md5(pk_val)

        self._text = kwargs.pop('text')

        super().__init__(*args, **kwargs)

    def _data_path(self, file_name):
        """Given a file name, form a relative path for a data file.

        Returns: str
        """
        prefix = self.text_hash[:3]
        suffix = self.text_hash[3:]

        # Form the file path.
        return os.path.join(self.corpus, prefix, suffix, file_name)

    def text_path(self):
        """Form the relative plain text bz2 path.

        Returns: str
        """
        return self._data_path('text.txt.bz2')

    def tokens_path(self):
        """Form the relative plain text bz2 path.

        Returns: str
        """
        return self._data_path('tokens.json.bz2')
