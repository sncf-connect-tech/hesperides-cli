import click
import json
from hesperidescli.client import Client


@click.command('events')
@click.option('--stream_name')
@click.option('--page')
@click.option('--size')
def command(stream_name, page, size):
    if not stream_name:  # if filename is not given
        print('stream_name required')
        return '[]'
    params = {'page': page, 'size': size}
    client = Client()
    response = client.get('/rest/events/' + stream_name, params)
    data = response.read()
    parsed = json.loads(data)
    print(json.dumps(parsed, indent=4, sort_keys=True))
