import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command('stats')
def command():
    client = Client()
    response = client.get('/rest/stats')
    utils.prettyprint(response)
