

from datetime import datetime as dt


def parse_date(text):
    """Parse an ECCO date string.
    """
    return dt.strptime(text, '%Y%m%d').date()
