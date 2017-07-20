import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.group('indexation')
def command():
    pass


@click.command('perform_reindex')
def perform_reindex():
    click.echo('Indexation hesperides')
    client = Client()
    response = client.post('/rest/indexation/perform_reindex')
    utils.prettyprint(response)


command.add_command(perform_reindex)
