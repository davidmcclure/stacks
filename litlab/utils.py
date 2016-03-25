

from bs4 import BeautifulSoup


def get_text(tree, selector):

    """
    Extract text from an element. Return None if the element is missing or the
    value is empty.

    Args:
        tree (BeautifulSoup): A bs4 tree.
        selector (str): A CSS selector.

    Returns:
        str|None
    """

    tag = tree.select_one(selector)

    if tag:
        return ' '.join(tag.stripped_strings) or None

    else:
        return None


def clone_tree(tree, parser='lxml'):

    """
    Create an copy of bs4 tree.

    Args:
        tree (BeautifulSoup): A bs4 tree.

    Returns: BeautifulSoup
    """

    return BeautifulSoup(str(tree), parser)
