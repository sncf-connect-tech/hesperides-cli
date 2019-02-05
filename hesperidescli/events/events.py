import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command("get-events")
@click.option("--stream-name", required=True)
@click.option("--page")
@click.option("--size")
def get_events(stream_name, page, size):
    params = {}
    if page:
        params["page"] = page
    if size:
        params["size"] = size
    response = Client().get("/rest/events/" + stream_name, params=params)
    utils.pretty_print(response)
