import click
import json
from hesperidescli.client import Client


@click.command('events')
@click.argument('stream_name')
@click.option('--page')
@click.option('--size')
def command(stream_name, page, size):
    params = {}
    if page is not None:
        params['page'] = page
    if size is not None:
        params['size'] = size
    client = Client()
    response = client.get('/rest/events/' + stream_name, params)
    data = response.read()
    parsed = json.loads(data)
    print(json.dumps(parsed, indent=4, sort_keys=True))
