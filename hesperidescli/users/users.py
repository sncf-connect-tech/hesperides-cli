import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command("get-user")
def get_user():
    response = Client().get("/rest/users/auth")
    utils.pretty_print(response)
