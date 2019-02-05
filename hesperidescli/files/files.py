import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command("get-files")
@click.option("--application-name", required=True)
@click.option("--platform-name", required=True)
@click.option("--path", required=True)
@click.option("--module-name", required=True)
@click.option("--module-version", required=True)
@click.option("--instance-name", required=True)
@click.option("--filename")
# pylint: disable=too-many-arguments
def get_files(
    application_name,
    platform_name,
    path,
    module_name,
    module_version,
    instance_name,
    filename,
):
    client = Client()
    if filename:
        response = client.get(
            "/files/applications/"
            + application_name
            + "/platforms/"
            + platform_name
            + "}/"
            + path
            + "/"
            + module_name
            + "/"
            + module_version
            + "/instances/"
            + instance_name
            + "/"
            + filename
        )
        utils.pretty_print(response)
    else:
        response = client.get(
            "/files/applications/"
            + application_name
            + "/platforms/"
            + platform_name
            + "}/"
            + path
            + "/"
            + module_name
            + "/"
            + module_version
            + "/instances/"
            + instance_name
        )
        utils.pretty_print(response)
