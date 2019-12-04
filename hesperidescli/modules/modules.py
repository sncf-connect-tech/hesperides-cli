import json
import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command("create-module")
@click.argument("body")
@click.option("--from-module-name")
@click.option("--from-module-version")
@click.option("--from-is-working-copy", is_flag=True)
def create_module(body, from_module_name, from_module_version, from_is_working_copy):
    params = {}
    if from_module_name is None and from_module_version:
        raise click.BadParameter(
            "--from-module-name required when --from-module-version is given"
        )
    if from_module_name and from_module_version is None:
        raise click.BadParameter(
            "--from-module-version required when --from-module-name is given"
        )
    if from_module_name:
        params["from_module_name"] = from_module_name
    if from_module_version:
        params["from_module_version"] = from_module_version
    if from_is_working_copy:
        params["from_is_working_copy"] = from_is_working_copy
    with open(body, "r") as body_file:
        file_body = body_file.read()
    response = Client().post("/rest/modules", params=params, body=file_body)
    utils.pretty_print(response)


@click.command("create-module-release")
@click.option("--module-name", required=True)
@click.option("--module-version", required=True)
@click.option("--release-version")
def create_module_release(module_name, module_version, release_version):
    params = {}
    params["module_name"] = module_name
    params["module_version"] = module_version
    params["release_version"] = release_version
    response = Client().post("/rest/modules/create_release", params=params)
    utils.pretty_print(response)


@click.command("create-module-workingcopy-template")
@click.argument("body")
@click.option("--module-name", required=True)
@click.option("--module-version", required=True)
def create_module_workingcopy_template(body, module_name, module_version):
    with open(body, "r") as body_file:
        file_body = body_file.read()
    response = _create_module_workingcopy_template(
        file_body, module_name, module_version
    )
    utils.pretty_print(response)


def _create_module_workingcopy_template(body, module_name, module_version):
    return Client().post(
        "/rest/modules/"
        + module_name
        + "/"
        + module_version
        + "/workingcopy/templates",
        body=body,
    )


@click.command("delete-module-release")
@click.option("--module-name", required=True)
@click.option("--module-version", required=True)
def delete_module_release(module_name, module_version):
    response = Client().delete(
        "/rest/modules/" + module_name + "/" + module_version + "/release"
    )
    utils.pretty_print(response)


@click.command("delete-module-workingcopy")
@click.option("--module-name", required=True)
@click.option("--module-version", required=True)
def delete_module_workingcopy(module_name, module_version):
    response = Client().delete(
        "/rest/modules/" + module_name + "/" + module_version + "/workingcopy"
    )
    utils.pretty_print(response)


@click.command("delete-module-workingcopy-template")
@click.option("--module-name", required=True)
@click.option("--module-version", required=True)
@click.option("--template-name", required=True)
def delete_module_workingcopy_template(module_name, module_version, template_name):
    response = Client().delete(
        "/rest/modules/"
        + module_name
        + "/"
        + module_version
        + "/workingcopy/templates/"
        + template_name
    )
    utils.pretty_print(response)


@click.command("get-module")
@click.option("--module-name", required=True)
@click.option("--module-version")
@click.option("--module-type")
def get_module(module_name, module_version, module_type):
    client = Client()
    if module_version is None and module_type is None:
        response = client.get("/rest/modules/" + module_name)
        utils.pretty_print(response)
    if module_version and module_type is None:
        response = client.get("/rest/modules/" + module_name + "/" + module_version)
        utils.pretty_print(response)
    if module_version and module_type:
        response = client.get(
            "/rest/modules/" + module_name + "/" + module_version + "/" + module_type
        )
        utils.pretty_print(response)


@click.command("get-module-release")
@click.option("--module-name", required=True)
@click.option("--module-version", required=True)
def get_module_release(module_name, module_version):
    response = Client().get(
        "/rest/modules/" + module_name + "/" + module_version + "/release"
    )
    utils.pretty_print(response)


@click.command("get-module-release-template")
@click.option("--module-name", required=True)
@click.option("--module-version", required=True)
@click.option("--template-name", required=True)
def get_module_release_template(module_name, module_version, template_name):
    response = _get_module_release_template(module_name, module_version, template_name)
    utils.pretty_print(response)


def _get_module_release_template(module_name, module_version, template_name):
    return Client().get(
        "/rest/modules/"
        + module_name
        + "/"
        + module_version
        + "/release/templates/"
        + template_name
    )


@click.command("get-module-release-templates")
@click.option("--module-name", required=True)
@click.option("--module-version", required=True)
def get_module_release_templates(module_name, module_version):
    response = Client().get(
        "/rest/modules/" + module_name + "/" + module_version + "/release/templates"
    )
    utils.pretty_print(response)


@click.command("get-module-workingcopy")
@click.option("--module-name", required=True)
@click.option("--module-version", required=True)
def get_module_workingcopy(module_name, module_version):
    response = Client().get(
        "/rest/modules/" + module_name + "/" + module_version + "/workingcopy"
    )
    utils.pretty_print(response)


@click.command("get-module-workingcopy-template")
@click.option("--module-name", required=True)
@click.option("--module-version", required=True)
@click.option("--template-name", required=True)
def get_module_workingcopy_template(module_name, module_version, template_name):
    response = _get_module_workingcopy_template(
        module_name, module_version, template_name
    )
    utils.pretty_print(response)


def _get_module_workingcopy_template(module_name, module_version, template_name):
    return Client().get(
        "/rest/modules/"
        + module_name
        + "/"
        + module_version
        + "/workingcopy/templates/"
        + template_name
    )


@click.command("get-module-workingcopy-templates")
@click.option("--module-name", required=True)
@click.option("--module-version", required=True)
def get_module_workingcopy_templates(module_name, module_version):
    response = Client().get(
        "/rest/modules/"
        + module_name
        + "/"
        + module_version
        + "/workingcopy/templates/"
    )
    utils.pretty_print(response)


@click.command("get-modules")
def get_modules():
    response = Client().get("/rest/modules/")
    utils.pretty_print(response)


@click.command("perform-search-modules")
@click.argument("terms")
def perform_search_modules(terms):
    params = {}
    params["terms"] = terms
    response = Client().get("/rest/modules/perform_search", params=params)
    utils.pretty_print(response)


@click.command("search-module")
@click.argument("terms")
def search_module(terms):
    params = {}
    params["temrs"] = terms
    response = Client().get("/rest/modules/search", params=params)
    utils.pretty_print(response)


@click.command("update-module")
@click.argument("body")
def update_module(body):
    with open(body, "r") as body_file:
        file_body = body_file.read()
    response = Client().put("/rest/modules/", body=file_body)
    utils.pretty_print(response)


@click.command("update-module-workingcopy-template")
@click.argument("body")
@click.option("--module-name", required=True)
@click.option("--module-version", required=True)
def update_module_workingcopy_template(body, module_name, module_version):
    with open(body, "r") as body_file:
        file_body = body_file.read()
    response = _update_module_workingcopy_template(
        file_body, module_name, module_version
    )
    utils.pretty_print(response)


def _update_module_workingcopy_template(body, module_name, module_version):
    return Client().put(
        "/rest/modules/"
        + module_name
        + "/"
        + module_version
        + "/workingcopy/templates",
        body=body,
    )


@click.command("upsert-module-workingcopy-template")
@click.argument("template-desc-filepath")
@click.option("--module-name", required=True)
@click.option("--module-version", required=True)
def upsert_module_workingcopy_template(
    template_desc_filepath, module_name, module_version
):
    with open(template_desc_filepath, "r") as template_desc_file:
        template_desc = json.load(template_desc_file)
    response = _get_module_workingcopy_template(
        module_name, module_version, template_desc["filename"]
    )
    if response.status_code == 200:
        template_desc["version_id"] = response.json()["version_id"]
        response = _update_module_workingcopy_template(
            json.dumps(template_desc), module_name, module_version
        )
    elif response.status_code == 404:
        template_desc["version_id"] = -1
        response = _create_module_workingcopy_template(
            json.dumps(template_desc), module_name, module_version
        )
    else:
        response.raise_for_status()
    utils.pretty_print(response)
