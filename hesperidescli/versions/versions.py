import click
import json
from hesperidescli.client import Client


@click.command('versions')
def command():
    client = Client()
    response = client.get('/rest/versions/')
    data = response.read()
    parsed = json.loads(data)
    print(json.dumps(parsed, indent=4, sort_keys=True))
