

import os
import anyconfig
import yaml

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from contextlib import contextmanager


class Config:

    @classmethod
    def from_env(cls, *extra_paths):

        """
        Get a config instance with the default files.

        Args:
            *extra_paths (str)
        """

        paths = [
            os.path.join(os.path.dirname(__file__), 'stacks.yml'),
            '/etc/stacks/stacks.yml'
        ]

        return cls(paths + list(extra_paths))

    def __init__(self, paths):

        """
        Initialize the configuration object.

        Args:
            paths (list): YAML paths, from most to least specific.
        """

        self.config = anyconfig.load(paths, ignore_missing=True)

    def __getitem__(self, key):

        """
        Get a configuration value.

        Args:
            key (str): The configuration key.

        Returns:
            The option value.
        """

        return self.config.get(key)

    def build_engine(self):

        """
        Build a SQLAlchemy engine.

        Returns: Engine
        """

        return create_engine(self['database_uri'])

    def build_sessionmaker(self):

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

        return scoped_session(self.build_sessionmaker())
