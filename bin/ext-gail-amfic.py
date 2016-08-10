#!/usr/bin/env python


import numpy as np
import json

from mpi4py import MPI

from stacks.ext_corpus import ExtCorpus
from stacks.adapters.gail_amfic import Corpus
from stacks.schemas import Text


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
        text = Text.from_gail_amfic(path)
        ext.flush(text)


if __name__ == '__main__':
    ext_gail_amfic()
