import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command("get-global-properties")
@click.option("--application-name", "--app", required=True)
@click.option("--platform-name", "--ptf", required=True)
@click.option("--timestamp")
def get_global_properties(application_name, platform_name, timestamp):
    params = {}
    params["path"] = "#"
    if timestamp:
        params["timestamp"] = "timestamp"
    response = Client().get(
        "/rest/applications/"
        + application_name
        + "/platforms/"
        + platform_name
        + "/properties",
        params=params,
    )
    utils.pretty_print(response)


@click.command("get-global-properties-usage")
@click.option("--application-name", "--app", required=True)
@click.option("--platform-name", "--ptf", required=True)
def get_global_properties_usage(application_name, platform_name):
    response = Client().get(
        "/rest/applications/"
        + application_name
        + "/platforms/"
        + platform_name
        + "/global_properties_usage"
    )
    utils.pretty_print(response)


@click.command("get-properties")
@click.option("--application-name", "--app", required=True)
@click.option("--platform-name", "--ptf", required=True)
@click.option("--path", required=True)
@click.option("--timestamp")
def get_properties(application_name, platform_name, path, timestamp):
    params = {}
    params["path"] = path
    if timestamp:
        params["timestamp"] = "timestamp"
    response = Client().get(
        "/rest/applications/"
        + application_name
        + "/platforms/"
        + platform_name
        + "/properties",
        params=params,
    )
    utils.pretty_print(response)


@click.command("get-properties-instance-model")
@click.option("--application-name", "--app", required=True)
@click.option("--platform-name", "--ptf", required=True)
def get_properties_instance_model(application_name, platform_name):
    response = Client().get(
        "/rest/applications/"
        + application_name
        + "/platforms/"
        + platform_name
        + "/properties/instance-model"
    )
    utils.pretty_print(response)
