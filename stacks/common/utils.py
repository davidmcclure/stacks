

import os

from contextlib import contextmanager


@contextmanager
def open_makedirs(fpath, *args, **kwargs):

    """
    Create the directory for a file, open it.
    """

    path = os.path.dirname(fpath)

    os.makedirs(path, exist_ok=True)

    with open(fpath, *args, **kwargs) as fh:
        yield fh
