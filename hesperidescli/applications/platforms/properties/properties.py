import string

import click
from click import secho

from hesperidescli import utils
from hesperidescli.client import Client


# Note: as of today, the following characters are valid in hesperides properties: !%"&'()+,-.:;?@[\]`~
VALID_EXPORTABLE_CHARS = string.ascii_letters + string.digits + "_"


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
@click.option(
    "--export",
    flag_value=True,
    default=False,
    help="Export properties for usage as environment variables in a shell",
)
def get_properties(application_name, platform_name, path, timestamp, export):
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
    if export:
        _export(response.json()["key_value_properties"])
    else:
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


def _export(key_value_properties):
    has_any_invalid_prop_name = False
    for property in key_value_properties:
        if all(c in VALID_EXPORTABLE_CHARS for c in property["name"]):
            print("export " + property["name"] + '="' + property["value"] + '"')
        else:
            secho(
                "[WARNING] Property name cannot be exported as it contains invalid characters: "
                + property["name"],
                err=True,
                fg="yellow",
            )
            has_any_invalid_prop_name = True
    if has_any_invalid_prop_name:
        raise click.Abort()
