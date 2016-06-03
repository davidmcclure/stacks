

import pytest
import yaml



def pytest_collect_file(parent, path):

    """
    Match yaml files.
    """

    if path.ext == '.yml':
        return YamlFile(path, parent)



class YamlFile(pytest.File):


    def collect(self):

        """
        Parse YAML, generate tests.
        """

        spec = yaml.safe_load(self.fspath.open())

        for id, fields in spec.items():
            yield YamlItem(id, self, fields)



class YamlItem(pytest.Item):


    def __init__(self, name, parent, fields):

        """
        Set the field definitions.
        """

        super().__init__(name, parent)

        self.fields = fields


    def runtest(self):

        """
        Assert the field specs.
        """

        print(self.fields)
