

import os
import anyconfig
import yaml

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.engine.url import URL
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

    @classmethod
    def from_test_env(cls):

        """
        Apply the testing configuration.
        """

        return cls.from_env('/etc/stacks/stacks.test.yml')

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

    def build_sqla_url(self):

        """
        Build a SQLAlchemy connection string.

        Returns: Engine
        """

        return URL(**self['database'])

    def build_sqla_engine(self):

        """
        Build a SQLAlchemy engine.

        Returns: Engine
        """

        url = self.build_sqla_url()

        return create_engine(url)

    def build_sqla_sessionmaker(self):

        """
        Build a SQLAlchemy session class.

        Returns: Session
        """

        return sessionmaker(bind=self.build_sqla_engine())

    def build_sqla_session(self):

        """
        Build a scoped session manager.

        Returns: Session
        """

        return scoped_session(self.build_sqla_sessionmaker())
