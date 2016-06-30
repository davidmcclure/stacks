

from .config import Config


config = Config.from_env()

session = config.build_session()
