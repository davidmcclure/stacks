

from schema import Schema


class ExtText:

    schema = Schema({
        'identifier': str,
        'title': str,
        'plain_text': str,
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

        pass
