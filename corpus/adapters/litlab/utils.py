

def parse_metadata(path):

    """
    Parse a metadata file.

    Args:
        path (str)

    Returns: dict
    """

    with open(path, mode='r', encoding='utf8') as fh:

        lines = fh.read().splitlines()

        return dict(map(lambda x: x.split('='), lines))
