

import hashlib

from schema import Schema, Optional


class ExtText:

    schema = Schema({

        'identifier': str,
        'title': str,
        'plain_text': str,

        Optional('author_name_full'): str,
        Optional('author_name_first'): str,
        Optional('author_name_last'): str,
        Optional('year'): int,

    })

    @classmethod
    def validate(cls, data):

        """
        Validate a text dict, return an instance.

        Args:
            data (dict)

        Returns: cls
        """

        return cls(cls.schema.validate(data))

    def __init__(self, data):

        """
        Set the data dict.

        Args:
            data (dict)
        """

        self.data = data

    def checksum(self):

        """
        Hash the identifier.

        Returns: str
        """

        md5 = hashlib.md5()

        md5.update(self.data['identifier'].encode('utf8'))

        return md5.hexdigest()
