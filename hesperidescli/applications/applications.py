import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command('get-application')
@click.option('--application_name')
def get_application(application_name):
    if application_name is None:
        print('--application_name required')
        return ''
    client = Client()
    response = client.get('/rest/applications/' + application_name)
    utils.pretty_print(response)


@click.command('get-application-from-module')
@click.option('--module')
@click.option('--version')
@click.option('--type')
def get_application_from_module(module, version, type):
    if module is None:
        print('--module required')
        return ''
    if version is None:
        print('--version required')
        return ''
    if type is None:
        print('--type required')
        return ''
    client = Client()
    response = client.get('/rest/applications/using_module/' + module + '/' + version + '/' + type)
    utils.pretty_print(response)


@click.command('perform-search-applications')
@click.option('--name')
def perform_search_applications(name):
    params = {}
    if name is None:
        print('--name required')
        return ''
    else:
        params['name'] = name
    client = Client()
    response = client.post('/rest/applications/perform_search?name=' + str(name), None)
    utils.pretty_print(response)
