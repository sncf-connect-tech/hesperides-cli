import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command("create-techno")
@click.argument("body")
@click.option("--from-name")
@click.option("--from-version")
@click.option("--from-is-working-copy", is_flag=True)
def create_techno(body, from_name, from_version, from_is_working_copy):
    params = {}
    if from_name is None and from_version:
        raise click.BadParameter("--from-name required when --from-version is given")
    if from_name and from_version is None:
        raise click.BadParameter("--from-version required when --from-name is given")
    params["from_name"] = from_name
    params["from_version"] = from_version
    params["from_is_working_copy"] = from_is_working_copy
    with open(body, "r") as body_file:
        file_body = body_file.read()
    response = Client().post("/rest/technos", params=params, body=file_body)
    utils.pretty_print(response)


@click.command("create-techno-workingcopy")
@click.argument("body")
@click.option("--name", required=True)
@click.option("--version", required=True)
@click.option("--template-name", required=True)
def create_techno_workingcopy(body, name, version, template_name):
    with open(body, "r") as body_file:
        file_body = body_file.read()
    response = Client().post(
        "/rest/technos/"
        + name
        + "/"
        + version
        + "/workingcopy/templates/"
        + template_name,
        body=file_body,
    )
    utils.pretty_print(response)


@click.command("delete-techno-release")
@click.option("--name", required=True)
@click.option("--version", required=True)
def delete_techno_release(name, version):
    response = Client().delete("/rest/technos/" + name + "/" + version + "/release")
    utils.pretty_print(response)


@click.command("delete-techno-workingcopy")
@click.option("--name", required=True)
@click.option("--version", required=True)
def delete_techno_workingcopy(name, version):
    response = Client().delete("/rest/technos/" + name + "/" + version + "/workingcopy")
    utils.pretty_print(response)


@click.command("get-techno-release")
@click.option("--name", required=True)
@click.option("--version", required=True)
@click.option("--template-name", required=True)
def get_techno_release(name, version, template_name):
    response = Client().get(
        "/rest/technos/" + name + "/" + version + "/release/templates/" + template_name
    )
    utils.pretty_print(response)


@click.command("get-techno-release-model")
@click.option("--name", required=True)
@click.option("--version", required=True)
def get_techno_release_model(name, version):
    response = Client().get("/rest/technos/" + name + "/" + version + "/release/model")
    utils.pretty_print(response)


@click.command("get-techno-workingcopy")
@click.option("--name", required=True)
@click.option("--version", required=True)
@click.option("--template-name", required=True)
def get_techno_workingcopy(name, version, template_name):
    response = Client().get(
        "/rest/technos/"
        + name
        + "/"
        + version
        + "/workingcopy/templates/"
        + template_name
    )
    utils.pretty_print(response)


@click.command("get-techno-workingcopy-model")
@click.option("--name", required=True)
@click.option("--version", required=True)
def get_techno_workingcopy_model(name, version):
    response = Client().get(
        "/rest/technos/" + name + "/" + version + "/workingcopy/model"
    )
    utils.pretty_print(response)


@click.command("get-technos-release")
@click.option("--name", required=True)
@click.option("--version", required=True)
def get_technos_release(name, version):
    response = Client().get(
        "/rest/technos/" + name + "/" + version + "/release/templates"
    )
    utils.pretty_print(response)


@click.command("get-technos-workingcopy")
@click.option("--name", required=True)
@click.option("--version", required=True)
def get_technos_workingcopy(name, version):
    response = Client().get(
        "/rest/technos/" + name + "/" + version + "/workingcopy/templates"
    )
    utils.pretty_print(response)


@click.command("perform-search-technos")
@click.argument("terms")
def perform_search_technos(terms):
    response = Client().get("/rest/technos/perform_search", params={"terms": terms})
    utils.pretty_print(response)


@click.command("update-techno-workingcopy")
@click.argument("body")
@click.option("--name", required=True)
@click.option("--version", required=True)
@click.option("--template-name", required=True)
def update_techno_workingcopy(body, name, version, template_name):
    with open(body, "r") as body_file:
        file_body = body_file.read()
    response = Client().put(
        "/rest/technos/"
        + name
        + "/"
        + version
        + "/workingcopy/templates/"
        + template_name,
        body=file_body,
    )
    utils.pretty_print(response)
