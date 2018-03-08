import configparser
import os
from os.path import expanduser


# pylint: disable=too-few-public-methods
class ConfigFile:
    _HOME = expanduser("~")
    _CONFIG_DIR = '.hesperides'
    _CONFIG_FILE_NAME = 'config'
    _CREDENTIALS_FILE_NAME = 'credentials'
    _CONFIG_FILE_PATH = _HOME + '/' + _CONFIG_DIR + '/' + _CONFIG_FILE_NAME
    _CREDENTIALS_FILE_PATH = _HOME + '/' + _CONFIG_DIR + '/' + _CREDENTIALS_FILE_NAME

    def __init__(self):
        self.config = configparser.ConfigParser()
        self._create_home()

    def _create_home(self):
        if not os.path.isdir(self._HOME + '/' + self._CONFIG_DIR):
            os.makedirs(self._HOME + '/' + self._CONFIG_DIR)
        with os.fdopen(os.open(self._HOME + '/' + self._CONFIG_DIR + '/' + self._CONFIG_FILE_NAME,
                               os.O_WRONLY | os.O_CREAT, 0o600), 'w'):
            pass
        with os.fdopen(os.open(self._HOME + '/' + self._CONFIG_DIR + '/' + self._CREDENTIALS_FILE_NAME,
                               os.O_WRONLY | os.O_CREAT, 0o600), 'w'):
            pass
