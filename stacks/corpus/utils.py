

import re


def slug_is_valid(slug):

    """
    Slugs can only contain letters, numbers, and underscores.

    Args:
        slug (str)

    Returns: bool
    """

    return bool(re.match('^[a-z0-9-]+$', slug))
