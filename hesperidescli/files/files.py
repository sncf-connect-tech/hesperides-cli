import os
from urllib.parse import quote

import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command(
    "get-files",
    help="If --name is provided, retrieve the file content, else list all files as a JSON array",
)
@click.option("--application-name", "--app", required=True)
@click.option("--platform-name", "--ptf", required=True)
@click.option("--path", required=True)
@click.option("--module-name", required=True)
@click.option("--module-version", required=True)
@click.option("--working-copy/--release", default=False)
@click.option("--instance-name")
@click.option("--name")
def get_files(**kwargs):
    client = Client()
    uri, params = _build_uri_and_params(**kwargs)
    if kwargs.get("name"):
        response = client.get(uri, params=params, accept="text/plain")
        response.raise_for_status()
        print(response.text)
    else:
        utils.pretty_print(client.get(uri, params=params))


@click.command(
    "write-files",
    help="Either --path + --module-name + --module-version must be provided, or all files are retrieved",
)
@click.option("--application-name", "--app", required=True)
@click.option("--platform-name", "--ptf", required=True)
@click.option("--path")
@click.option("--module-name")
@click.option("--module-version")
@click.option("--working-copy/--release", default=None)
@click.option("--instance-name")
def write_files(**kwargs):
    client = Client()
    module_keys = _get_module_keys(**kwargs)
    for module_key in module_keys:
        kwargs.update(module_key)
        # pylint: disable=using-constant-test
        if module_keys:
            click.secho(
                "Processing module: {module_name}#{module_version}#{wc}".format(
                    wc=_wc2str(kwargs["working_copy"]), **kwargs
                ),
                fg="green",
            )
        uri, params = _build_uri_and_params(**kwargs)
        for file in client.get(uri, params=params).json():
            response = client.get(
                uri + "/" + file["name"], params=params, accept="text/plain"
            )
            response.raise_for_status()
            os.makedirs(os.path.dirname(file["location"]), exist_ok=True)
            click.secho(
                'Generating file "{}" from template named "{}"'.format(
                    file["location"], file["name"]
                ),
                fg="blue",
            )
            with open(file["location"], "w") as generated_file:
                generated_file.write(response.text)
            chmod(file["location"], file["rights"])


# pylint: disable=too-many-arguments
def _build_uri_and_params(
    application_name,
    platform_name,
    path,
    module_name,
    module_version,
    working_copy,
    instance_name=None,
    name=None,
):
    params = {
        "isWorkingCopy": "true" if working_copy else "false",
        "template_namespace": "modules#{}#{}#{}".format(
            module_name, module_version, _wc2str(working_copy)
        ),  # this query param is in fact not necessary if "name" is not provided
        "simulate": "false",
    }
    if not instance_name:
        instance_name = "default"
        params["simulate"] = "true"
    uri = (
        "/rest/applications/"
        + application_name
        + "/platforms/"
        + platform_name
        + "/"
        + quote(path)
        + "/"
        + module_name
        + "/"
        + module_version
        + "/instances/"
        + instance_name
        + "/files"
    )
    if name:
        uri += "/" + name
    return uri, params


def _get_module_keys(
    application_name,
    platform_name,
    path=None,
    module_name=None,
    module_version=None,
    working_copy=None,
    instance_name=None,
):
    if path and module_name and module_version and working_copy is not None:
        return [
            {
                "path": path,
                "module_name": module_name,
                "module_version": module_version,
                "working_copy": working_copy,
                "instance_name": instance_name,
            }
        ]
    response = Client().get(
        "/rest/applications/" + application_name + "/platforms/" + platform_name
    )
    response.raise_for_status()
    module_keys = []
    for module in response.json()["modules"]:
        module_keys.append(
            {
                "path": module["path"],
                "module_name": module["name"],
                "module_version": module["version"],
                "working_copy": module["working_copy"],
                "instances": [
                    m["name"] for m in module["instances"]
                ],  # only needed for filtering below
            }
        )
    if path:
        module_keys = list(filter(lambda key: key["path"] == path, module_keys))
    if module_name:
        module_keys = list(
            filter(lambda key: key["module_name"] == module_name, module_keys)
        )
    if module_version:
        module_keys = list(
            filter(lambda key: key["module_version"] == module_version, module_keys)
        )
    if working_copy is not None:
        module_keys = list(
            filter(lambda key: key["working_copy"] == working_copy, module_keys)
        )
    if instance_name:
        module_keys = list(
            filter(lambda key: instance_name in key["instances"], module_keys)
        )
        if module_keys:  # else error management will be performed below
            assert len(module_keys) == 1
            module_keys[0]["instance_name"] = instance_name
    if not module_keys:
        raise click.BadParameter(
            "Zero matching module(s) found given the --path / --module-name / --module-version / --working-copy / --release / --instance-name options provided"
        )
    for module_key in module_keys:
        del module_key["instances"]  # should not be exposed outside this function
    return module_keys


def _wc2str(working_copy):
    return "WORKINGCOPY" if working_copy else "RELEASE"


def chmod(filepath, rights):
    mode, power = 0, 1
    for scope in ("other", "group", "user"):
        perms = rights.get(scope, "").strip()
        if "x" in perms:
            mode |= 0o1 * power
        if "w" in perms:
            mode |= 0o2 * power
        if "r" in perms:
            mode |= 0o4 * power
        power *= 8
    if not mode:
        mode = 0o644
    click.echo("Setting file permissions to: {:o}".format(mode))
    os.chmod(filepath, mode)
