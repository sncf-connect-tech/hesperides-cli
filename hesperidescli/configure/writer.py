from hesperidescli.configure.configfile import ConfigFile


class ConfigFileWriter(ConfigFile):
    def update_config(self, new_values):
        self._create_home()
        self.config['default'] = new_values
        self._write_config(self.config)

    def update_credentials(self, new_values):
        self._create_home()
        self.config['default'] = new_values
        self._write_credentials(self.config)

    def _write_config(self, config):
        with open(self._HOME + '/' + self._CONFIG_DIR + '/' + self._CONFIG_FILE_NAME, 'w') as configfile:
            config.write(configfile)

    def _write_credentials(self, config):
        with open(self._HOME + '/' + self._CONFIG_DIR + '/' + self._CREDENTIALS_FILE_NAME, 'w') as configfile:
            config.write(configfile)
