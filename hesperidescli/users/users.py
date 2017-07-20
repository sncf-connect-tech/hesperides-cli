import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command('users')
def command():
    client = Client()
    response = client.get('/rest/users/auth')
    utils.prettyprint(response)
