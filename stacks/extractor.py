

import numpy as np
import ujson
import logging

from stacks.corpus import Corpus


class Extractor:

    def __init__(self):
        """Initialize the corpus adapter.
        """
        self.corpus = Corpus.from_env()

    def args(self):
        """Provide a list of arguments for each text source.

        Returns: list
        """
        raise NotImplementedError

    def flush(self):
        """Flush a text.
        """
        raise NotImplementedError

    def __call__(self):
        """Scatter args, flush results.
        """
        from mpi4py import MPI

        comm = MPI.COMM_WORLD

        size = comm.Get_size()
        rank = comm.Get_rank()

        segments = None

        # ** Scatter path segments.

        if rank == 0:

            segments = [
                ujson.dumps(list(s))
                for s in np.array_split(self.args(), size)
            ]

        segment = comm.scatter(segments, root=0)

        # ** Write JSON files.

        args = ujson.loads(segment)

        print(rank, len(args))

        for i, arg in enumerate(args):

            try:

                if type(arg) == dict:
                    self.flush(**arg)

                else:
                    self.flush(arg)

            except Exception as e:
                logging.exception('message')

            if i % 100 == 0:
                print(rank, i)
