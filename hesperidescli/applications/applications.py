import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command('applications-perform-search')
@click.option('--name')
def applications_perform_search(name):
    params = {}
    if name is None:
        print('--name required')
        return ''
    else:
        params['name'] = name
    client = Client()
    response = client.get('/rest/applications/perform_search', params)
    utils.prettyprint(response)


@click.command('get-application')
@click.option('--application_name')
def get_application(application_name):
    if application_name is None:
        print('--application_name required')
        return ''
    client = Client()
    response = client.get('/rest/applications/' + application_name)
    utils.prettyprint(response)


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
    utils.prettyprint(response)

