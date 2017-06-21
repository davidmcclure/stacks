

from .config import Config


config = Config.read()

session = config.build_sqla_session()
