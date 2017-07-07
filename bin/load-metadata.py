#!/usr/bin/env python


import numpy as np
import json

from datetime import datetime as dt

from stacks import config, session
from stacks.metadata.models import Text, reset_db
from stacks.utils import grouper

from stacks.ext import (
    Text as ExtText,
    Corpus as ExtCorpus,
)


def load_metadata(n=1000):
    """Clear the metadata database and gather text rows.
    """
    from mpi4py import MPI

    comm = MPI.COMM_WORLD

    size = comm.Get_size()
    rank = comm.Get_rank()

    # ** Scatter path segments.

    segments = None

    if rank == 0:

        corpus = ExtCorpus.from_env()

        # Log dir walk duration.

        print(dt.now().isoformat())

        paths = list(corpus.paths())

        print(dt.now().isoformat())

        segments = [
            json.dumps(list(s))
            for s in np.array_split(paths, size)
        ]

    # ** Build text rows.

    segment = comm.scatter(segments, root=0)

    # Parse the segment.
    paths = json.loads(segment)

    print(rank, len(paths))

    page = []
    for i, path in enumerate(paths):

        text = ExtText.from_bz2_json(path)

        row = text.to_native('metadata')
        row['path'] = path

        page.append(row)

        if i%100 == 0:
            print(rank, i)

    # ** Flush to disk.

    pages = comm.gather(page, root=0)

    if rank == 0:

        # Loop through ranks.
        i = 0
        for page in pages:

            groups = grouper(page, n);

            # Bulk-insert rows in groups.
            for group in groups:
                session.bulk_insert_mappings(Text, group)
                i += n
                print(i)

        session.commit()


if __name__ == '__main__':
    load_metadata()
