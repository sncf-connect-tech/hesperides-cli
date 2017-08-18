import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command('get-module')
@click.option('--module_name')
@click.option('--module_version')
@click.option('--module_type')
def get_module(module_name, module_version, module_type):
    if module_name is None:
        print('--module_name required')
        return ''
    if module_type and module_version is None:
        print('--module_version required')
        return ''
    client = Client()
    if module_type is None and module_version is None:
        response = client.get('/rest/modules/' + module_name)
        utils.pretty_print(response)
    if module_type and module_version is None:
        response = client.get('/rest/modules/' + module_name + '/' + module_type)
        utils.pretty_print(response)
    if module_type and module_version:
        response = client.get('/rest/modules/' + module_name + '/' + module_type + '/' + module_version)
        utils.pretty_print(response)


@click.command('get-modules')
def get_modules():
    client = Client()
    response = client.get('/rest/modules/')
    utils.pretty_print(response)


@click.command('get-release-module')
@click.option('--module_name')
@click.option('--module_version')
def get_release_module(module_name, module_version):
    if module_name is None:
        print('--module_name required')
        return ''
    if module_version is None:
        print('--module_version required')
        return ''
    client = Client()
    response = client.get('/rest/modules/' + module_name + '/' + module_version + '/release')
    utils.pretty_print(response)
