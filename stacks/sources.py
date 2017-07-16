

import attr

from bs4 import BeautifulSoup


@attr.s
class XMLSource:

    xml = attr.ib()

    @classmethod
    def from_file(cls, path):
        """Hydrate from a file path.

        Args:
            path (str)

        Returns: cls
        """
        with open(path, 'r') as fh:
            return cls(BeautifulSoup(fh, 'xml'))
