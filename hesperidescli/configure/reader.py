from configparser import NoOptionError, Error as ConfigParserError

import click

from hesperidescli.configure.configfile import ConfigFile


class ConfigFileReader(ConfigFile):
    _DEFAULT_SENTINEL = object()

    def get_profile(self):
        try:
            return self.get_config_item("profile")
        except (ConfigParserError, KeyError):
            raise click.UsageError(
                'No profile has been configured. Please type "hesperides set-conf"'
            )

    def get_config_item(self, *args, **kwargs):
        self.config.read(self._CONFIG_FILE_PATH)
        return self._get(*args, **kwargs)

    def get_credentials_item(self, *args, **kwargs):
        self.config.read(self._CREDENTIALS_FILE_PATH)
        return self._get(*args, **kwargs)

    def _get(self, *args, default=_DEFAULT_SENTINEL):
        if len(args) == 1:
            args = ("config", args[0])
        try:
            # pylint: disable=no-value-for-parameter
            return self.config.get(*args)
        except NoOptionError:
            if default is not self._DEFAULT_SENTINEL:
                return default
            raise

    def print_config(self):
        self._print(self._CONFIG_FILE_PATH)

    def print_credentials(self):
        self._print(self._CREDENTIALS_FILE_PATH)

    def _print(self, file_path):
        click.secho("#{}:".format(file_path))
        self.config.read(file_path)
        with open(file_path, "r") as config_file:
            click.secho(config_file.read())
