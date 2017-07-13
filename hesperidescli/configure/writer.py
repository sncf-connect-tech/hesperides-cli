import os
from os.path import expanduser


class ConfigFileWriter:
    CONFIG_DIR = '.hesperides'
    CONFIG_FILE_NAME = 'credentials'

    def update_config(self, new_values):
        self._create_home()

    def _create_home(self):
        home = expanduser("~")
        if not os.path.isdir(home + '/' + self.CONFIG_DIR):
            os.makedirs(home + '/' + self.CONFIG_DIR)
        with os.fdopen(os.open(home + '/' + self.CONFIG_DIR + '/' + self.CONFIG_FILE_NAME,
                               os.O_WRONLY | os.O_CREAT, 0o600), 'w'):
            pass
