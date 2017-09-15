import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command('perform-indexation-all')
def perform_indexation_all():
    client = Client()
    response = client.post('/rest/indexation/all')
    utils.pretty_print(response)


@click.command('perform-indexation-applications')
def perform_indexation_applications():
    client = Client()
    response = client.post('/rest/indexation/applications')
    utils.pretty_print(response)


@click.command('perform-indexation-mapping')
def perform_indexation_mapping():
    client = Client()
    response = client.post('/rest/indexation/mapping')
    utils.pretty_print(response)


@click.command('perform-indexation-modules')
def perform_indexation_modules():
    client = Client()
    response = client.post('/rest/indexation/modules')
    utils.pretty_print(response)


@click.command('perform-indexation-modules-templates')
def perform_indexation_modules_templates():
    client = Client()
    response = client.post('/rest/indexation/modules/templates')
    utils.pretty_print(response)


@click.command('perform-indexation-templates-packages')
def perform_indexation_templates_packages():
    client = Client()
    response = client.post('/rest/indexation/templates/packages')
    utils.pretty_print(response)
