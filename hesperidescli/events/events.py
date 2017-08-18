import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command('get-events')
@click.option('--stream_name')
@click.option('--page')
@click.option('--size')
def get_events(stream_name, page, size):
    params = {}
    if page is not None:
        params['page'] = page
    if size is not None:
        params['size'] = size
    client = Client()
    response = client.get('/rest/events/' + stream_name, params)
    utils.pretty_print(response)
