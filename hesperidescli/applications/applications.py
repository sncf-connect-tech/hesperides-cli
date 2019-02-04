import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command("get-application")
@click.option("--application_name")
def get_application(application_name):
    if application_name is None:
        print("--application_name required")
        raise click.Abort()
    client = Client()
    response = client.get("/rest/applications/" + application_name)
    utils.pretty_print(response)


@click.command("get-applications-using-module")
@click.option("--module")
@click.option("--version")
@click.option("--type")
def get_applications_using_module(module, version, type):
    if module is None:
        print("--module required")
        raise click.Abort()
    if version is None:
        print("--version required")
        raise click.Abort()
    if type is None:
        print("--type required")
        raise click.Abort()
    client = Client()
    response = client.get(
        "/rest/applications/using_module/" + module + "/" + version + "/" + type
    )
    utils.pretty_print(response)


@click.command("perform-search-applications")
@click.option("--name")
def perform_search_applications(name):
    params = {}
    if name is None:
        print("--name required")
        raise click.Abort()
    else:
        params["name"] = name
    client = Client()
    response = client.post("/rest/applications/perform_search", params=params)
    utils.pretty_print(response)
