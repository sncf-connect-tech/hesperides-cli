import click

from hesperidescli import utils
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
    utils.prettyprint(response)


command.add_command(hipchat)
