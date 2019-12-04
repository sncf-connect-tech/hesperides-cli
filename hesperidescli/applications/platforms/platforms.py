import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command("create-application-platform")
@click.argument("body")
@click.option("--application-name", "--app", required=True)
@click.option("--from-application")
@click.option("--from-platform")
def create_application_platform(
    body, application_name, from_application, from_platform
):
    if from_application is None and from_platform:
        raise click.BadParameter(
            "--from-application required when --from-platform is given"
        )
    if from_application and from_platform is None:
        raise click.BadParameter(
            "--from-platform required when --from-application is given"
        )
    with open(body, "r") as body_file:
        file_body = body_file.read()
    response = Client().post(
        "/rest/applications/" + application_name + "/platforms", body=file_body
    )
    utils.pretty_print(response)


@click.command("delete-application-platform")
@click.option("--application-name", "--app", required=True)
@click.option("--platform-name", "--ptf", required=True)
def delete_application_platform(application_name, platform_name):
    response = Client().delete(
        "/rest/applications/" + application_name + "/platforms/" + platform_name
    )
    utils.pretty_print(response)


@click.command("get-application-platform")
@click.option("--application-name", "--app", required=True)
@click.option("--platform-name", "--ptf", required=True)
def get_application_platform(application_name, platform_name):
    response = Client().get(
        "/rest/applications/" + application_name + "/platforms/" + platform_name
    )
    utils.pretty_print(response)


@click.command("perform-search-application-platforms")
@click.option("--application-name", "--app", required=True)
@click.option("--platform-name", "--ptf")
def perform_search_application_platforms(application_name, platform_name):
    params = {}
    params["applicationName"] = application_name
    if platform_name:
        params["platformName"] = platform_name
    response = Client().get(
        "/rest/applications/platforms/perform_search", params=params
    )
    utils.pretty_print(response)


@click.command("update-application-platform")
@click.argument("body")
@click.option("--application-name", "--app", required=True)
@click.option("--copy-properties-for-upgraded", is_flag=True)
def update_application_platform(
    body, application_name, copy_properties_for_upgraded_modules
):
    params = {}
    if copy_properties_for_upgraded_modules:
        params[
            "copy_properties_for_upgraded_modules"
        ] = copy_properties_for_upgraded_modules
    with open(body, "r") as body_file:
        file_body = body_file.read()
    response = Client().put(
        "/rest/applications/" + application_name + "/platforms",
        params=params,
        body=file_body,
    )
    utils.pretty_print(response)
