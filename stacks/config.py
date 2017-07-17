

import os

from cleanconfig import CleanConfig
from voluptuous import Schema, Required

from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.engine.url import URL


class Config(CleanConfig):

    name = 'stacks'

    config_dirs = [
        os.path.dirname(__file__),
        '/share/PI/malgeehe/config/stacks',
        '/etc/stacks',
    ]

    schema = Schema({

        'database': {
            Required('drivername'): str,
            Required('database'): str,
        },

        'data': {
            Required('raw'): str,
            Required('ext'): str,
        },

    })

    # TODO: separate db module?

    def build_sqla_url(self):
        """Build a SQLAlchemy connection string.

        Returns: Engine
        """
        return URL(**self['database'])

    def build_sqla_engine(self):
        """Build a SQLAlchemy engine.

        Returns: Engine
        """
        url = self.build_sqla_url()

        engine = create_engine(url)

        # Fix transaction bugs in pysqlite.
        # http://docs.sqlalchemy.org/en/rel_1_0/dialects/sqlite.html#pysqlite-serializable

        @event.listens_for(engine, 'connect')
        def on_connect(conn, record):
            conn.execute('pragma foreign_keys=ON')
            conn.isolation_level = None

        @event.listens_for(engine, 'begin')
        def on_begin(conn):
            conn.execute('BEGIN')

        return engine

    def build_sqla_sessionmaker(self):
        """Build a SQLAlchemy session class.

        Returns: Session
        """
        return sessionmaker(bind=self.build_sqla_engine())

    def build_sqla_session(self):
        """Build a scoped session manager.

        Returns: Session
        """
        return scoped_session(self.build_sqla_sessionmaker())
