#!/usr/bin/env python


import numpy as np
import json

from mpi4py import MPI

from stacks.ext_corpus import ExtCorpus
from stacks.adapters.ecco import Corpus, Text


def ext_ecco():

    """
    Extract ECCO.
    """

    comm = MPI.COMM_WORLD

    size = comm.Get_size()
    rank = comm.Get_rank()

    segments = None

    # ** Scatter path segments.

    if rank == 0:

        corpus = Corpus.from_env()

        paths = list(corpus.text_paths())

        segments = [
            json.dumps(list(s))
            for s in np.array_split(paths, size)
        ]

    segment = comm.scatter(segments, root=0)

    # ** Write JSON files.

    paths = json.loads(segment)

    ext = ExtCorpus.from_env()

    for path in paths:

        try:
            ext.flush_ecco(path)

        except Exception as e:
            print(e)


if __name__ == '__main__':
    ext_ecco()
