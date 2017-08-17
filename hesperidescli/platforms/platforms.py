import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command('create-application-platforms')
@click.option('--application_name')
@click.option('--from_application')
@click.option('--from_platform')
@click.option('--body')
def create_application_platforms(application_name, from_application, from_platform, body):
    if application_name is None:
        print('--application_name required')
        return ''
    if from_application is None and from_platform:
        print('--from_application required when --from_platform is given')
        return ''
    if from_application and from_platform is None:
        print('--from_platform required when --from_application is given')
        return ''
    if body is None:
        print('--body required')
        return ''
    file = open(body, "r")
    file_body = file.read()
    file.close()
    client = Client()
    response = client.post('/rest/applications/' + application_name + '/platforms', file_body)
    utils.prettyprint(response)


@click.command('delete-application-platforms')
@click.option('--application_name')
@click.option('--platform_name')
def delete_application_platforms(application_name, platform_name):
    if application_name is None:
        print('--application_name required')
        return ''
    if platform_name is None:
        print('--platform_name required')
        return ''
    client = Client()
    response = client.delete('/rest/applications/' + application_name + '/platforms/' + platform_name)
    utils.prettyprint(response)


@click.command('get-application-platforms')
@click.option('--application_name')
@click.option('--platform_name')
def get_application_platforms(application_name, platform_name):
    if application_name is None:
        print('--application_name required')
        return ''
    if platform_name is None:
        print('--platform_name required')
        return ''
    client = Client()
    response = client.get('/rest/applications/' + application_name + '/platforms/' + platform_name)
    utils.prettyprint(response)


@click.command('update-application-platforms')
@click.option('--application_name')
@click.option('--copy_properties_for_upgraded_modules', is_flag=True)
@click.option('--body')
def update_application_platforms(application_name, copy_properties_for_upgraded_modules, body):
    if application_name is None:
        print('--application_name required')
        return ''
    if body is None:
        print('--body required')
        return ''
    file = open(body, "r")
    file_body = file.read()
    file.close()
    client = Client()
    response = client.put(
        '/rest/applications/' + application_name + '/platforms?copyPropertiesForUpgradedModules='
        + copy_properties_for_upgraded_modules, file_body)
    utils.prettyprint(response)
