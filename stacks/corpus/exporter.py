

from stacks.common.singletons import config
from stacks.corpus.models import Export


class Exporter:

    def from_env(cls, export):

        """
        Make an exported from the ENV-defined data path.

        Args:
            export (Export)
        """

        return cls(config['export_path'], export)

    def __init__(self, path, export):

        """
        Construct the text query.

        Args:
            path (str)
            export (Export)
        """

        pass
