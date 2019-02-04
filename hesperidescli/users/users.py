import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command("get-user")
def get_user():
    client = Client()
    response = client.get("/rest/users/auth")
    utils.pretty_print(response)
