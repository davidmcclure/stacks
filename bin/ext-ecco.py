#!/usr/bin/env python


import numpy as np
import json

from mpi4py import MPI

from stacks.ext_corpus import ExtCorpus
from stacks.adapters.ecco import Corpus
from stacks.schemas import Text


class Extractor:

    def __init__(self):

        """
        Initialize the `ext` wrapper.
        """

        self.corpus = ExtCorpus.from_env()

    def args(self):

        """
        Provide a list of arguments for each text source.

        Returns: list
        """

        corpus = Corpus.from_env()

        return list(corpus.text_paths())

    def flush(self, path):

        """
        Flush a text.

        Args:
            path (str)
        """

        text = Text.from_ecco(path)

        self.corpus.flush(text)

    def __call__(self):

        """
        Scatter args, flush results.
        """

        comm = MPI.COMM_WORLD

        size = comm.Get_size()
        rank = comm.Get_rank()

        segments = None

        # ** Scatter path segments.

        if rank == 0:

            segments = [
                json.dumps(list(s))
                for s in np.array_split(self.args(), size)
            ]

        segment = comm.scatter(segments, root=0)

        # ** Write JSON files.

        for arg in json.loads(segment):
            self.flush(arg)


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
        text = Text.from_ecco(path)
        ext.flush(text)


if __name__ == '__main__':
    Extractor()()
    # extractor()
