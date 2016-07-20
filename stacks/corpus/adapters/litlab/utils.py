

import re


def parse_metadata(path):

    """
    Parse a metadata file.

    Args:
        path (str)

    Returns: dict
    """

    # name_first=David
    pattern = re.compile('^(?P<key>.*)=(?P<val>.*)$')

    with open(path, mode='r', encoding='utf8') as fh:

        lines = fh.read().splitlines()

        params = {}
        for line in lines:

            match = pattern.match(line)

            if match:
                key = match.group('key')
                val = match.group('val')
                params[key] = val

        return dict(params)
