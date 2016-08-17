#!/usr/bin/env python


import numpy as np
import json

from mpi4py import MPI

from stacks.extractor import Extractor
from stacks.raw.gail_amfic import Corpus, Text
from stacks.ext import Corpus as ExtCorpus


def ext_gail_amfic():

    """
    Gail American Fiction
    """

    comm = MPI.COMM_WORLD

    size = comm.Get_size()
    rank = comm.Get_rank()

    segments = None

    # ** Scatter path segments.

    if rank == 0:

        corpus = Corpus.from_env()

        args = list(corpus.text_paths())

        segments = [
            json.dumps(list(s))
            for s in np.array_split(args, size)
        ]

    segment = comm.scatter(segments, root=0)

    # ** Write JSON files.

    args = json.loads(segment)

    print(len(args))

    ext = ExtCorpus.from_env()

    for i, arg in enumerate(args):

        try:

            text = Text(arg)

            ext.insert_text(text.to_ext_text())

        except Exception as e:
            print(arg, e)

        if i%100 == 0:
            print(rank, i)


# class GailAmficExtractor(Extractor):

    # def args(self):

        # """
        # Provide a list of ECCO paths.

        # Returns: list
        # """

        # corpus = Corpus.from_env()

        # return list(corpus.text_paths())

    # def flush(self, path):

        # """
        # Flush a text.

        # Args:
            # path (str)
        # """

        # text = Text(path)

        # self.corpus.insert_text(text.to_ext_text())


if __name__ == '__main__':
    # GailAmficExtractor()()
    ext_gail_amfic()
