import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command('get-versions')
def get_versions():
    client = Client()
    response = client.get('/rest/versions/')
    utils.prettyprint(response)
