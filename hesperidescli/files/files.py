import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command('get-files')
@click.option('--application_name')
@click.option('--platform_name')
@click.option('--path')
@click.option('--module_name')
@click.option('--module_version')
@click.option('--instance_name')
@click.option('--filename')
# pylint: disable=too-many-arguments
def get_files(application_name, platform_name, path, module_name, module_version, instance_name, filename):
    if application_name is None:
        print('--application_name required')
        raise click.Abort()
    if platform_name is None:
        print('--platform_name required')
        raise click.Abort()
    if path is None:
        print('--path required')
        raise click.Abort()
    if module_name is None:
        print('--module_name required')
        raise click.Abort()
    if module_version is None:
        print('--module_version required')
        raise click.Abort()
    if instance_name is None:
        print('--instance_name required')
        raise click.Abort()
    client = Client()
    if filename:
        response = client.get(
            '/files/applications/' + application_name + '/platforms/' + platform_name + '}/' + path + '/' + module_name
            + '/' + module_version + '/instances/' + instance_name + '/' + filename)
        utils.pretty_print(response)
    else:
        response = client.get(
            '/files/applications/' + application_name + '/platforms/' + platform_name + '}/' + path + '/' + module_name
            + '/' + module_version + '/instances/' + instance_name)
        utils.pretty_print(response)
