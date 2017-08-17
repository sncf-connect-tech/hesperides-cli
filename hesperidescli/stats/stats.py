import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command('get-stats')
def get_stats():
    client = Client()
    response = client.get('/rest/stats')
    utils.prettyprint(response)
