import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command('perform-reindex')
def perform_reindex():
    client = Client()
    response = client.post('/rest/indexation/perform_reindex')
    utils.prettyprint(response)
