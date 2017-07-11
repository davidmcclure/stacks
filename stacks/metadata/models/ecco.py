

import os
import bz2

from cityhash import CityHash32

from sqlalchemy.inspection import inspect

from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String,
    UniqueConstraint,
    Text,
    DateTime,
    Date,
)

from stacks.metadata.models import Base


# TODO: Make generic.
class Text:

    corpus = Column(String, nullable=False)

    text_hash = Column(String, nullable=False)

    def __init__(self, *args, **kwargs):
        """Set the corpus name, hash PK.
        """
        # Get PK column name.
        pk_col = inspect(ECCOText).primary_key[0].name
        pk_val = kwargs[pk_col]

        # Mirror table name, hash the PK.
        self.corpus = self.__tablename__
        self.text_hash = str(CityHash32(str(pk_val)))

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


class ECCOText(Text, Base):

    __tablename__ = 'ecco_text'

    document_id = Column(String, primary_key=True)

    estc_id = Column(String)

    unit = Column(Integer)

    reel = Column(Integer)

    mcode = Column(String)

    pub_date = Column(Date)

    release_date = Column(Date)

    source_bib_citation = Column(String)

    source_library = Column(String)

    language = Column(String)

    module = Column(String)

    document_type = Column(String)

    notes = Column(String)

    author_marc_name = Column(String)

    author_birth_date = Column(Integer)

    author_death_date = Column(Integer)

    author_marc_date = Column(String)

    full_title = Column(String)

    display_title = Column(String)

    imprint_full = Column(String)

    imprint_city = Column(String)

    imprint_publisher = Column(String)

    imprint_year = Column(Integer)

    collation = Column(String)

    publication_place = Column(String)

    total_pages = Column(Integer)


class ECCOSubjectHead(Base):

    __tablename__ = 'ecco_subject_head'

    id = Column(Integer, primary_key=True)

    document_id = Column(String)

    type = Column(String)

    sub_field = Column(String)

    value = Column(String)
