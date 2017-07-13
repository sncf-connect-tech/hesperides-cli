from hesperidescli.configure.configfile import ConfigFile


class ConfigFileReader(ConfigFile):
    def get_config(self):
        self.config.read(self._HOME + '/' + self._CONFIG_DIR + '/' + self._CONFIG_FILE_NAME)
        return self.config['default']

    def get_credentials(self):
        self.config.read(self._HOME + '/' + self._CONFIG_DIR + '/' + self._CREDENTIALS_FILE_NAME)
        return self.config['default']
