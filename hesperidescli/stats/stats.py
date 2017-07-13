import click
import json
from hesperidescli.client import Client


@click.command('stats')
def command():
    client = Client()
    response = client.call('/rest/stats')
    data = response.read()
    parsed = json.loads(data)
    print(json.dumps(parsed, indent=4, sort_keys=True))
