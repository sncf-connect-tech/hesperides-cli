import configparser
import os
from os.path import expanduser, join


# pylint: disable=too-few-public-methods
class ConfigFile:
    _CONFIG_DIR = join(expanduser("~"), ".hesperides")
    _CONFIG_FILE_PATH = join(_CONFIG_DIR, "config")
    _CREDENTIALS_FILE_PATH = join(_CONFIG_DIR, "credentials")

    def __init__(self):
        self.config = configparser.ConfigParser()
        self._create_home()

    def _create_home(self):
        if not os.path.isdir(self._CONFIG_DIR):
            os.makedirs(self._CONFIG_DIR)
        with os.fdopen(
            os.open(self._CONFIG_FILE_PATH, os.O_WRONLY | os.O_CREAT, 0o600), "w"
        ):
            pass
        with os.fdopen(
            os.open(self._CREDENTIALS_FILE_PATH, os.O_WRONLY | os.O_CREAT, 0o600), "w"
        ):
            pass
