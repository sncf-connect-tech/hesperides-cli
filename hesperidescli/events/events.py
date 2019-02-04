import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command("get-events")
@click.option("--stream_name")
@click.option("--page")
@click.option("--size")
def get_events(stream_name, page, size):
    params = {}
    if page:
        params["page"] = page
    if size:
        params["size"] = size
    client = Client()
    response = client.get("/rest/events/" + stream_name, params=params)
    utils.pretty_print(response)
