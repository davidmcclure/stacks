

import os
import glob

from litlab.conf import settings



class Corpus:


    @classmethod
    def from_env(cls):

        """
        Wrap the settings-defined path.
        """

        return cls(settings.LITLAB_CHADH_ENGLISH_DRAMA)


    def __init__(self, path):

        """
        Set the corpus path.

        Args:
            path (str): The corpus path.
        """

        self.path = os.path.abspath(path)


    def texts(self):

        """
        Generate text text metadata.

        Yields:
            dict: Properties for the each text.
        """

        for path in glob.glob(os.path.join(self.path, '*.new')):
            yield Text(path)



class Text:


    def __init__(self, path):

        """
        Parse the XML.

        Args:
            path (str): The text path.
        """

        pass
