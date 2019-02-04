import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command("create-application-platform")
@click.option("--application_name")
@click.option("--from_application")
@click.option("--from_platform")
@click.option("--body")
def create_application_platform(
    application_name, from_application, from_platform, body
):
    if application_name is None:
        print("--application_name required")
        raise click.Abort()
    if from_application is None and from_platform:
        print("--from_application required when --from_platform is given")
        raise click.Abort()
    if from_application and from_platform is None:
        print("--from_platform required when --from_application is given")
        raise click.Abort()
    if body is None:
        print("--body required")
        raise click.Abort()
    file = open(body, "r")
    file_body = file.read()
    file.close()
    client = Client()
    response = client.post(
        "/rest/applications/" + application_name + "/platforms", body=file_body
    )
    utils.pretty_print(response)


@click.command("delete-application-platform")
@click.option("--application_name")
@click.option("--platform_name")
def delete_application_platform(application_name, platform_name):
    if application_name is None:
        print("--application_name required")
        raise click.Abort()
    if platform_name is None:
        print("--platform_name required")
        raise click.Abort()
    client = Client()
    response = client.delete(
        "/rest/applications/" + application_name + "/platforms/" + platform_name
    )
    utils.pretty_print(response)


@click.command("get-application-platform")
@click.option("--application_name")
@click.option("--platform_name")
def get_application_platform(application_name, platform_name):
    if application_name is None:
        print("--application_name required")
        raise click.Abort()
    if platform_name is None:
        print("--platform_name required")
        raise click.Abort()
    client = Client()
    response = client.get(
        "/rest/applications/" + application_name + "/platforms/" + platform_name
    )
    utils.pretty_print(response)


@click.command("perform-search-application-platforms")
@click.option("--application_name")
@click.option("--platform_name")
def perform_search_application_platforms(application_name, platform_name):
    params = {}
    if application_name is None:
        print("--application_name required")
        raise click.Abort()
    params["application_name"] = application_name
    if platform_name:
        params["platform_name"] = platform_name
    client = Client()
    response = client.post("/rest/applications/platforms/perform_search", params=params)
    utils.pretty_print(response)


@click.command("update-application-platform")
@click.option("--application_name")
@click.option("--copy_properties_for_upgraded_modules", is_flag=True)
@click.option("--body")
def update_application_platform(
    application_name, copy_properties_for_upgraded_modules, body
):
    params = {}
    if application_name is None:
        print("--application_name required")
        raise click.Abort()
    if body is None:
        print("--body required")
        raise click.Abort()
    if copy_properties_for_upgraded_modules:
        params[
            "copy_properties_for_upgraded_modules"
        ] = copy_properties_for_upgraded_modules
    file = open(body, "r")
    file_body = file.read()
    file.close()
    client = Client()
    response = client.put(
        "/rest/applications/" + application_name + "/platforms",
        params=params,
        body=file_body,
    )
    utils.pretty_print(response)
