import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command('get-global-properties')
@click.option('--application_name')
@click.option('--platform_name')
@click.option('--timestamp')
def get_global_properties(application_name, platform_name, timestamp):
    params = {}
    if application_name is None:
        print('--application_name required')
        return ''
    if platform_name is None:
        print('--platform_name required')
        return ''
    params['path'] = '#'
    if timestamp:
        params['timestamp'] = timestamp
    client = Client()
    response = client.get(
        '/rest/applications/' + application_name + '/platforms/' + platform_name + '/properties', params)
    utils.pretty_print(response)


@click.command('get-global-properties-usage')
@click.option('--application_name')
@click.option('--platform_name')
def get_global_properties_usage(application_name, platform_name):
    if application_name is None:
        print('--application_name required')
        return ''
    if platform_name is None:
        print('--platform_name required')
        return ''
    client = Client()
    response = client.get(
        '/rest/applications/' + application_name + '/platforms/' + platform_name + '/global_properties_usage')
    utils.pretty_print(response)


@click.command('get-properties')
@click.option('--application_name')
@click.option('--platform_name')
@click.option('--path')
@click.option('--timestamp')
def get_properties(application_name, platform_name, path, timestamp):
    params = {}
    if application_name is None:
        print('--application_name required')
        return ''
    if platform_name is None:
        print('--platform_name required')
        return ''
    if path is None:
        print('--path required')
        return ''
    else:
        params['path'] = path
    if timestamp:
        params['timestamp'] = timestamp
    client = Client()
    response = client.get(
        '/rest/applications/' + application_name + '/platforms/' + platform_name + '/properties', params)
    utils.pretty_print(response)


@click.command('get-properties-instance-model')
@click.option('--application_name')
@click.option('--platform_name')
def get_properties_instance_model(application_name, platform_name):
    if application_name is None:
        print('--application_name required')
        return ''
    if platform_name is None:
        print('--platform_name required')
        return ''
    client = Client()
    response = client.get(
        '/rest/applications/' + application_name + '/platforms/' + platform_name + '/properties/instance-model')
    utils.pretty_print(response)
