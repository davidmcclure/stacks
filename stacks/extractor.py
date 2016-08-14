

import numpy as np
import json

from mpi4py import MPI

from stacks.ext import Corpus


class Extractor:

    def __init__(self):

        """
        Initialize the `ext` wrapper.
        """

        self.corpus = Corpus.from_env()

    def args(self):

        """
        Provide a list of arguments for each text source.

        Returns: list
        """

        raise NotImplementedError

    def flush(self):

        """
        Flush a text.
        """

        raise NotImplementedError

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

            try:

                if type(arg) == dict:
                    self.flush(**arg)

                else:
                    self.flush(arg)

            except Exception as e:
                print(arg, e)
