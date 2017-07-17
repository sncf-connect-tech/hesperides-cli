import click
import json
from hesperidescli.client import Client


@click.group('feedback')
def command():
    pass


@click.command('hipchat')
@click.option('--message')
@click.option('--note')
def hipchat(message, note):
    click.echo('Feedback Hipchat hesperides')
    feedback = {}
    if message:
        feedback = message
    if note:
        feedback = "{ \"feedback\": { \"note\": \"" + note + "\" } }"
    client = Client()
    response = client.post('/rest/feedback/hipchat', feedback)
    data = response.read()
    parsed = json.loads(data)
    print(json.dumps(parsed, indent=4, sort_keys=True))


command.add_command(hipchat)
