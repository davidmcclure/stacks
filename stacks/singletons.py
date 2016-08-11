

from .config import Config
from .utils import git_rev


config = Config.from_env()

session = config.build_sqla_session()

version = git_rev()
