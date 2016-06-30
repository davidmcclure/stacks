

import os
import anyconfig
import yaml

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from contextlib import contextmanager


class Config:

    @classmethod
    def from_env(cls):

        """
        Get a config instance with the default files.
        """

        cwd = os.path.dirname(__file__)

        return cls([
            os.path.join(cwd, 'base.yml'),
            # TODO: prod, dev
        ])

    def __init__(self, paths):

        """
        Initialize the configuration object.

        Args:
            paths (list): YAML paths, from most to least specific.
        """

        self.paths = paths

        self.read()

    def __getitem__(self, key):

        """
        Get a configuration value.

        Args:
            key (str): The configuration key.

        Returns:
            The option value.
        """

        return self.config.get(key)

    def read(self):

        """
        Read the configuration files.
        """

        self.config = anyconfig.load(self.paths, ignore_missing=True)

    def build_engine(self):

        """
        Build a SQLAlchemy engine.

        Returns: Engine
        """

        return create_engine(self['database_uri'])

    def build_session_factory(self):

        """
        Build a SQLAlchemy session class.

        Returns: Session
        """

        return sessionmaker(bind=self.build_engine())

    def build_session(self):

        """
        Build a scoped session manager.

        Returns: Session
        """

        return scoped_session(self.build_session_factory())
