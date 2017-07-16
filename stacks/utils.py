

import re
import scandir
import os
import logging

from datetime import datetime as dt

from nltk.tokenize import WordPunctTokenizer
from nltk import pos_tag


def scan_paths(root, pattern):
    """Walk a directory and gather up all file paths with a given extension.

    Args:
        root (str): The top-level directory.
        pattern (str): A filename regex.

    Yields: str
    """
    pattern = re.compile(pattern)

    for root, dirs, files in scandir.walk(root, followlinks=True):
        for name in files:

            # Match the extension.
            if pattern.search(name):
                yield os.path.join(root, name)


def get_text(tree, selector):
    """Extract text from an element. Return None if the element is missing or
    the value is empty.

    Args:
        tree (BeautifulSoup): A bs4 tree.
        selector (str): A CSS selector.

    Returns: str|None
    """
    tag = tree.select_one(selector)

    return ' '.join(tag.stripped_strings) or None


def tokenize(text):
    """Tokenize a raw text.

    Args:
        text (str)

    Returns: list of {token, char1, char2, pos}
    """
    tokenizer = WordPunctTokenizer()

    # Get token character spans.
    spans = list(tokenizer.span_tokenize(text))

    # Materialize the token stream.
    tokens = [text[c1:c2] for c1, c2 in spans]

    # Tag parts-of-speech.
    tags = pos_tag(tokens)

    return [

        dict(
            token=token.lower(),
            char1=c1,
            char2=c2,
            pos=pos,
        )

        for (c1, c2), token, (_, pos) in
        zip(spans, tokens, tags)

    ]


def try_or_log(f):
    """Wrap a class method call in a try block. If an error is raised, return
    None and log the exception.
    """
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            # TODO|dev
            # logging.exception('message')
            return None
    return wrapper


def parse_year(text):
    """Extract a 4-digit year integer from a string.

    Returns: int
    """
    return int(re.search('[0-9]{4}', text).group(0))


def parse_8d_date(text):
    """Parse a date string.
    """
    return dt.strptime(text, '%Y%m%d').date()
