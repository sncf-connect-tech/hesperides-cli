from configparser import NoSectionError, NoOptionError

import sys

from hesperidescli.configure.configfile import ConfigFile


class ConfigFileReader(ConfigFile):
    def get_config(self, section):
        self._get(self._CONFIG_FILE_PATH, section)

    def get_credentials(self, section):
        self._get(self._CREDENTIALS_FILE_PATH, section)

    def get_item(self, section, item):
        return self.config.get(section, item)

    def get_profile(self):
        try:
            self.get_config('config')
            return self.get_item('config', 'profile')
        except (NoSectionError, NoOptionError):
            print('No profile has been configured')
            sys.exit(1)

    def print_config(self):
        self._print(self._CONFIG_FILE_PATH)

    def print_credentials(self):
        self._print(self._CREDENTIALS_FILE_PATH)

    def _get(self, file_path, section):
        self.config.read(file_path)
        try:
            return self.config.items(section)
        except KeyError:
            raise Exception('hesperides has not been configured. Please type "hesperides set-conf"')

    def _print(self, file_path):
        self.config.read(file_path)
        file = open(file_path, "r")
        print(file.read())
        file.close()
