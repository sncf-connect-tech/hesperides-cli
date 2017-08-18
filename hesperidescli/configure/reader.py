from hesperidescli.configure.configfile import ConfigFile


class ConfigFileReader(ConfigFile):
    def get_config(self):
        self.config.read(self._HOME + '/' + self._CONFIG_DIR + '/' + self._CONFIG_FILE_NAME)
        try:
            return self.config['default']
        except KeyError:
            raise Exception('hesperides-cli has not been configured. Please type "hesperides configure set".')

    def get_credentials(self):
        self.config.read(self._HOME + '/' + self._CONFIG_DIR + '/' + self._CREDENTIALS_FILE_NAME)
        try:
            return self.config['default']
        except KeyError:
            raise Exception('hesperides-cli has not been configured. Please type "hesperides configure set".')

    def print_config(self):
        self.config.read(self._HOME + '/' + self._CONFIG_DIR + '/' + self._CONFIG_FILE_NAME)
        file = open(self._HOME + '/' + self._CONFIG_DIR + '/' + self._CONFIG_FILE_NAME, "r")
        print(file.read())
        file.close()

    def print_credentials(self):
        self.config.read(self._HOME + '/' + self._CONFIG_DIR + '/' + self._CREDENTIALS_FILE_NAME)
        file = open(self._HOME + '/' + self._CONFIG_DIR + '/' + self._CREDENTIALS_FILE_NAME, "r")
        print(file.read())
        file.close()
