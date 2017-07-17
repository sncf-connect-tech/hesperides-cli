import click
import json
from hesperidescli.client import Client


@click.group('feedback')
def command():
    pass


@click.command('hipchat')
@click.argument('message')
def hipchat(message):
    click.echo('Feedback Hipchat hesperides')
    client = Client()
    response = client.post('/rest/feedback/hipchat', message)
    data = response.read()
    parsed = json.loads(data)
    print(json.dumps(parsed, indent=4, sort_keys=True))


command.add_command(hipchat)
