#!/usr/bin/env python


import numpy as np
import json

from mpi4py import MPI

from stacks.corpus.ext_corpus import ExtCorpus
from stacks.corpus.adaptes.gail_amfic.corpus import Corpus
from stacks.corpus.adaptes.gail_amfic.text import Text


def ext_gail_amfic():

    """
    Index year -> token -> offset -> count.
    """

    comm = MPI.COMM_WORLD

    size = comm.Get_size()
    rank = comm.Get_rank()

    segments = None

    # Get JSON-encoded path segments.
    if rank == 0:

        corpus = Corpus.from_env()

        paths = list(corpus.text_paths())

        segments = [
            json.dumps(list(s))
            for s in np.array_split(paths, size)
        ]

    segment = comm.scatter(segments, root=0)

    paths = json.loads(segment)

    ext = ExtCorpus.from_env()

    for path in paths:

        text = Text(path)

        ext_text = ExtText.validate(text.as_ext_text())

        ext.flush(ext_text)


if __name__ == '__main__':
    ext_gail_amfic()
