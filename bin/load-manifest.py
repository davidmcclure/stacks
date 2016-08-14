#!/usr/bin/env python


from stacks import config
from stacks.metadata.models import Text, reset_db


def load_manifest():

    """
    Clear the metadata database and gather text rows.
    """

    reset_db()

    Text.ingest()


if __name__ == '__main__':
    load_manifest()
