import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command("get-applications")
def get_applications():
    response = Client().get("/rest/applications")
    utils.pretty_print(response)


@click.command("get-application")
@click.argument("application-name")
def get_application(application_name):
    response = Client().get("/rest/applications/" + application_name)
    utils.pretty_print(response)


# pylint: disable=redefined-builtin
@click.command("get-applications-using-module")
@click.option("--module", required=True)
@click.option("--version", required=True)
@click.option("--type", required=True)
def get_applications_using_module(module, version, type):
    response = Client().get(
        "/rest/applications/using_module/" + module + "/" + version + "/" + type
    )
    utils.pretty_print(response)


@click.command("perform-search-applications")
@click.argument("name")
def perform_search_applications(name):
    params = {"name": name}
    response = Client().get("/rest/applications/perform_search", params=params)
    utils.pretty_print(response)
