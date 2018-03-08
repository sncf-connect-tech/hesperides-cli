import base64
import click

from hesperidescli.configure.reader import ConfigFileReader
from hesperidescli.configure.writer import ConfigFileWriter


@click.command('delete-profile')
@click.option('--profile_name')
def delete_profile(profile_name):
    if profile_name is None:
        print('--profile_name required')
        raise click.Abort()
    config_writer = ConfigFileWriter()
    config_writer.remove_config_section(profile_name)
    reader = ConfigFileReader()
    if reader.get_profile() == profile_name:
        config_writer.remove_profile()
    credentials_writer = ConfigFileWriter()
    credentials_writer.remove_credentials_section(profile_name)


@click.command('get-conf')
def get_conf():
    config_reader = ConfigFileReader()
    config_reader.print_config()
    config_reader.print_credentials()


@click.command('get-profile')
def get_profile():
    reader = ConfigFileReader()
    print(reader.get_profile())


def get_config(key):
    profile = ConfigFileReader().get_profile()
    reader = ConfigFileReader()
    # config = reader.get_config(profile)
    # config = reader.get_credentials(profile)
    return reader.get_item(profile, key)


@click.command('set-conf')
@click.option('--profile', prompt=True, hide_input=False, confirmation_prompt=False, default='default')
@click.option('--username', prompt=True, hide_input=False, confirmation_prompt=False, default='')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=False, default='')
@click.option('--hesperides_endpoint', prompt=True, hide_input=False, confirmation_prompt=False,
              default='https://hesperides')
@click.option('--response_format', prompt=False, hide_input=False, confirmation_prompt=False, default='json')
def set_conf(profile, username, password, hesperides_endpoint, response_format):
    basic_auth = base64.b64encode(str.encode('%s:%s' % (username, password))).decode('UTF-8')
    config = {'endpoint': hesperides_endpoint, 'format': response_format}
    credentials = {'username': username, 'auth': basic_auth}
    config_writer = ConfigFileWriter()
    config_writer.update_config(profile, config, False)
    credentials_writer = ConfigFileWriter()
    credentials_writer.update_credentials(profile, credentials, False)
    config_writer.update_config('config', {}, False)


@click.command('set-profile')
@click.option('--profile_name')
def set_profile(profile_name):
    if profile_name is None:
        print('--profile_name required')
        raise click.Abort()
    config_writer = ConfigFileWriter()
    config = {'profile': profile_name}
    config_writer.update_config('config', config, True)
