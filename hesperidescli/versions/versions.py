import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command('versions')
def command():
    client = Client()
    response = client.get('/rest/versions/')
    utils.prettyprint(response)
