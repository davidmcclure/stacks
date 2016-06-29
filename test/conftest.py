

import pytest

from stacks import config as _config
from stacks.models import Base


@pytest.fixture(scope='session', autouse=True)
def test_config():

    """
    Register the testing config file.
    """

    _config.paths.append('~/.stacks.test.yml')
    _config.build()


@pytest.fixture()
def db(config):

    """
    Create / reset the testing database.
    """

    engine = config.build_engine()

    BaseModel.metadata.drop_all(engine)
    BaseModel.metadata.create_all(engine)
