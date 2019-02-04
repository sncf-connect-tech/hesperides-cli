from configparser import Error as ConfigParserError

import sys

from hesperidescli.configure.configfile import ConfigFile


class ConfigFileReader(ConfigFile):
    def get_profile(self):
        try:
            return self.get_config_item("config", "profile")
        except ConfigParserError:
            print("No profile has been configured")
            sys.exit(1)

    def get_config_item(self, *args):
        self.config.read(self._CONFIG_FILE_PATH)
        return self._get(*args)

    def get_credentials_item(self, *args):
        self.config.read(self._CREDENTIALS_FILE_PATH)
        return self._get(*args)

    def _get(self, *args):
        try:
            return self.config.get(*args)
        except KeyError:
            raise Exception(
                'hesperides has not been configured. Please type "hesperides set-conf"'
            )

    def print_config(self):
        self._print(self._CONFIG_FILE_PATH)

    def print_credentials(self):
        self._print(self._CREDENTIALS_FILE_PATH)

    def _print(self, file_path):
        self.config.read(file_path)
        file = open(file_path, "r")
        print(file.read())
        file.close()
