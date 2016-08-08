#!/usr/bin/env python


import numpy as np
import json

from mpi4py import MPI

from stacks.corpus.ext_corpus import ExtCorpus
from stacks.corpus.adapters.gail_amfic.corpus import Corpus
from stacks.corpus.adapters.gail_amfic.text import Text


def ext_gail_amfic():

    """
    Extract Gail American Fiction.
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
        ext.flush_gail_amfic(path)


if __name__ == '__main__':
    ext_gail_amfic()
