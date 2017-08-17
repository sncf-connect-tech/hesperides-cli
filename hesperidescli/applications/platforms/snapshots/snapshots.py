import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command('get-snapshots')
@click.option('--application_name')
@click.option('--platform_name')
def get_snapshots(application_name, platform_name):
    if application_name is None:
        print('--application_name required')
        return ''
    if platform_name is None:
        print('--platform_name required')
        return ''
    client = Client()
    response = client.get('/rest/applications/' + application_name + '/platforms/' + platform_name + '/snapshots')
    utils.prettyprint(response)


@click.command('restore-snapshot')
@click.option('--application_name')
@click.option('--platform_name')
def restore_snapshot(application_name, platform_name):
    if application_name is None:
        print('--application_name required')
        return ''
    if platform_name is None:
        print('--platform_name required')
        return ''
    client = Client()
    response = client.post(
        '/rest/applications/' + application_name + '/platforms/' + platform_name + '/restore_snapshot')
    utils.prettyprint(response)


@click.command('take-snapshot')
@click.option('--application_name')
@click.option('--platform_name')
@click.option('--body')
def take_snapshot(application_name, platform_name, body):
    if application_name is None:
        print('--application_name required')
        return ''
    if platform_name is None:
        print('--platform_name required')
        return ''
    if body is None:
        print('--body required')
        return ''
    file = open(body, "r")
    file_body = file.read()
    file.close()
    client = Client()
    response = client.post(
        '/rest/applications/' + application_name + '/platforms/' + platform_name + '/take_snapshot', file_body)
    utils.prettyprint(response)
