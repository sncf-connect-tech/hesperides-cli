import click
import json
from hesperidescli.client import Client


@click.group('indexation')
def command():
    pass


@click.command('perform_reindex')
def perform_reindex():
    click.echo('Indexation hesperides')
    client = Client()
    response = client.post('/rest/indexation/perform_reindex')
    data = response.read()
    parsed = json.loads(data)
    print(json.dumps(parsed, indent=4, sort_keys=True))


command.add_command(perform_reindex)
