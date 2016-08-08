#!/usr/bin/env python


from mpi4py import MPI


def ext_gail_amfic():

    """
    Index year -> token -> offset -> count.
    """

    comm = MPI.COMM_WORLD

    size = comm.Get_size()
    rank = comm.Get_rank()

    # get path list
    # split into `size` chunks
    # scatter
    # write JSON files


if __name__ == '__main__':
    ext_gail_amfic()
