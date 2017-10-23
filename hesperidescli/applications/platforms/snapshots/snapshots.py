import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command('get-application-platform-snapshots')
@click.option('--application_name')
@click.option('--platform_name')
def get_application_platform_snapshots(application_name, platform_name):
    if application_name is None:
        print('--application_name required')
        raise click.Abort()
    if platform_name is None:
        print('--platform_name required')
        raise click.Abort()
    client = Client()
    response = client.get('/rest/applications/' + application_name + '/platforms/' + platform_name + '/snapshots')
    utils.pretty_print(response)


@click.command('restore-application-platform-snapshots')
@click.option('--application_name')
@click.option('--platform_name')
def restore_application_platform_snapshots(application_name, platform_name):
    if application_name is None:
        print('--application_name required')
        raise click.Abort()
    if platform_name is None:
        print('--platform_name required')
        raise click.Abort()
    client = Client()
    response = client.post(
        '/rest/applications/' + application_name + '/platforms/' + platform_name + '/restore_snapshot')
    utils.pretty_print(response)


@click.command('take-application-platform-snapshot')
@click.option('--application_name')
@click.option('--platform_name')
@click.option('--body')
def take_application_platform_snapshot(application_name, platform_name, body):
    if application_name is None:
        print('--application_name required')
        raise click.Abort()
    if platform_name is None:
        print('--platform_name required')
        raise click.Abort()
    if body is None:
        print('--body required')
        raise click.Abort()
    file = open(body, "r")
    file_body = file.read()
    file.close()
    client = Client()
    response = client.post(
        '/rest/applications/' + application_name + '/platforms/' + platform_name + '/take_snapshot', body=file_body)
    utils.pretty_print(response)
