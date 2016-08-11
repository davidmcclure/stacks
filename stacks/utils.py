

import re
import scandir
import os
import subprocess
import hashlib


def scan_paths(root, pattern):

    """
    Walk a directory and gather up all file paths with a given extension.

    Args:
        root (str): The top-level directory.
        pattern (str): A filename regex.

    Yields: str
    """

    pattern = re.compile(pattern)

    for root, dirs, files in scandir.walk(root):
        for name in files:

            # Match the extension.
            if pattern.search(name):
                yield os.path.join(root, name)


def get_text(tree, selector):

    """
    Extract text from an element. Return None if the element is missing or the
    value is empty.

    Args:
        tree (BeautifulSoup): A bs4 tree.
        selector (str): A CSS selector.

    Returns: str|None
    """

    tag = tree.select_one(selector)

    if tag:
        return ' '.join(tag.stripped_strings) or None

    else:
        return None


def checksum(value):

    """
    Checksum a string.

    Args:
        value (str)

    Returns: str
    """

    md5 = hashlib.md5()

    md5.update(value.encode('utf8'))

    return md5.hexdigest()


def git_rev():

    """
    Get the hash of the git HEAD.

    Returns: str
    """

    head = subprocess.check_output(['git', 'rev-parse', 'HEAD'])

    return head.strip().decode()
