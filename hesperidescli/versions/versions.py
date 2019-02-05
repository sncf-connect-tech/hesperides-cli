import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command("get-versions")
def get_versions():
    response = Client().get("/rest/versions/")
    utils.pretty_print(response)
