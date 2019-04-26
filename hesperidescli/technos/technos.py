import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command("create-techno")
@click.argument("body")
@click.option("--from-package-name")
@click.option("--from-package-version")
@click.option("--from-is-working-copy", is_flag=True)
def create_techno(
    body, from_package_name, from_package_version, from_is_working_copy
):
    params = {}
    if from_package_name is None and from_package_version:
        raise click.BadParameter(
            "--from-package-name required when --from-package-version is given"
        )
    if from_package_name and from_package_version is None:
        raise click.BadParameter(
            "--from-package-version required when --from-package-name is given"
        )
    params["from_package_name"] = from_package_name
    params["from_package_version"] = from_package_version
    params["from_is_working_copy"] = from_is_working_copy
    with open(body, "r") as body_file:
        file_body = body_file.read()
    response = Client().post("/rest/technos", params=params, body=file_body)
    utils.pretty_print(response)


@click.command("create-techno-workingcopy")
@click.argument("body")
@click.option("--package-name", required=True)
@click.option("--package-version", required=True)
@click.option("--template-name", required=True)
def create_techno_workingcopy(
    body, package_name, package_version, template_name
):
    with open(body, "r") as body_file:
        file_body = body_file.read()
    response = Client().post(
        "/rest/technos/"
        + package_name
        + "/"
        + package_version
        + "/workingcopy/templates/"
        + template_name,
        body=file_body,
    )
    utils.pretty_print(response)


@click.command("delete-techno-release")
@click.option("--package-name", required=True)
@click.option("--package-version", required=True)
def delete_techno_release(package_name, package_version):
    response = Client().delete(
        "/rest/technos/" + package_name + "/" + package_version + "/release"
    )
    utils.pretty_print(response)


@click.command("delete-techno-workingcopy")
@click.option("--package-name", required=True)
@click.option("--package-version", required=True)
def delete_techno_workingcopy(package_name, package_version):
    response = Client().delete(
        "/rest/technos/"
        + package_name
        + "/"
        + package_version
        + "/workingcopy"
    )
    utils.pretty_print(response)


@click.command("get-techno-release")
@click.option("--package-name", required=True)
@click.option("--package-version", required=True)
@click.option("--template-name", required=True)
def get_techno_release(package_name, package_version, template_name):
    response = Client().get(
        "/rest/technos/"
        + package_name
        + "/"
        + package_version
        + "/release/templates/"
        + template_name
    )
    utils.pretty_print(response)


@click.command("get-techno-release-model")
@click.option("--package-name", required=True)
@click.option("--package-version", required=True)
def get_techno_release_model(package_name, package_version):
    response = Client().get(
        "/rest/technos/"
        + package_name
        + "/"
        + package_version
        + "/release/model"
    )
    utils.pretty_print(response)


@click.command("get-techno-workingcopy")
@click.option("--package-name", required=True)
@click.option("--package-version", required=True)
@click.option("--template-name", required=True)
def get_techno_workingcopy(package_name, package_version, template_name):
    response = Client().get(
        "/rest/technos/"
        + package_name
        + "/"
        + package_version
        + "/workingcopy/templates/"
        + template_name
    )
    utils.pretty_print(response)


@click.command("get-techno-workingcopy-model")
@click.option("--package-name", required=True)
@click.option("--package-version", required=True)
def get_techno_workingcopy_model(package_name, package_version):
    response = Client().get(
        "/rest/technos/"
        + package_name
        + "/"
        + package_version
        + "/workingcopy/model"
    )
    utils.pretty_print(response)


@click.command("get-technos-release")
@click.option("--package-name", required=True)
@click.option("--package-version", required=True)
def get_technos_release(package_name, package_version):
    response = Client().get(
        "/rest/technos/"
        + package_name
        + "/"
        + package_version
        + "/release/templates"
    )
    utils.pretty_print(response)


@click.command("get-technos-workingcopy")
@click.option("--package-name", required=True)
@click.option("--package-version", required=True)
def get_technos_workingcopy(package_name, package_version):
    response = Client().get(
        "/rest/technos/"
        + package_name
        + "/"
        + package_version
        + "/workingcopy/templates"
    )
    utils.pretty_print(response)


@click.command("perform-search-technos")
@click.argument("terms")
def perform_search_technos(terms):
    response = Client().get(
        "/rest/technos/perform_search", params={"terms": terms}
    )
    utils.pretty_print(response)


@click.command("update-techno-workingcopy")
@click.argument("body")
@click.option("--package-name", required=True)
@click.option("--package-version", required=True)
@click.option("--template-name", required=True)
def update_techno_workingcopy(
    body, package_name, package_version, template_name
):
    with open(body, "r") as body_file:
        file_body = body_file.read()
    response = Client().put(
        "/rest/technos/"
        + package_name
        + "/"
        + package_version
        + "/workingcopy/templates/"
        + template_name,
        body=file_body,
    )
    utils.pretty_print(response)
