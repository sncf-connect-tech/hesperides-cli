import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command('post-feedback')
@click.option('--message')
@click.option('--note')
def post_feedback(message, note):
    feedback = {}
    if message:
        feedback = message
    if note:
        feedback = "{ \"feedback\": { \"note\": \"" + note + "\" } }"
    client = Client()
    response = client.post('/rest/feedback/hipchat', feedback)
    utils.pretty_print(response)
