#!/usr/bin/env python


import numpy as np
import json

from stacks import config, session
from stacks.metadata.models import Text, reset_db
from stacks.utils import grouper

from stacks.ext import (
    Text as ExtText,
    Corpus as ExtCorpus,
)


def load_metadata():

    """
    Clear the metadata database and gather text rows.
    """

    from mpi4py import MPI

    comm = MPI.COMM_WORLD

    size = comm.Get_size()
    rank = comm.Get_rank()

    # ** Scatter path segments.

    segments = None

    if rank == 0:

        corpus = ExtCorpus.from_env()

        paths = list(corpus.paths())

        segments = [
            json.dumps(list(s))
            for s in np.array_split(paths, size)
        ]

    segment = comm.scatter(segments, root=0)

    # ** Build text rows.

    page = []
    for path in json.loads(segment):

        text = ExtText.from_bz2_json(path)

        row = text.to_native('metadata')
        row['path'] = path

        page.append(row)

    # ** Flush to disk.

    pages = comm.gather(page, root=0)

    # Flatten out the row list.
    rows = [r for page in pages for r in page]

    if rank == 0:

        for group in grouper(rows, 1000):
            session.bulk_insert_mappings(Text, group)

        session.commit()


if __name__ == '__main__':
    load_metadata()
