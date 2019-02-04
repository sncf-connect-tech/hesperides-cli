import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command("create-template-package")
@click.option("--from-package-name")
@click.option("--from-package-version")
@click.option("--from-is-working-copy", is_flag=True)
@click.option("--body")
def create_template_package(
    from_package_name, from_package_version, from_is_working_copy, body
):
    params = {}
    if from_package_name is None and from_package_version:
        print("--from-package-name required when --from-package-version is given")
        raise click.Abort()
    if from_package_name and from_package_version is None:
        print("--from-package-version required when --from-package-name is given")
        raise click.Abort()
    if body is None:
        print("--body required")
        raise click.Abort()
    params["from_package_name"] = from_package_name
    params["from_package_version"] = from_package_version
    params["from_is_working_copy"] = from_is_working_copy
    file = open(body, "r")
    file_body = file.read()
    file.close()
    client = Client()
    response = client.post("/rest/templates/packages", params=params, body=file_body)
    utils.pretty_print(response)


@click.command("create-template-package-workingcopy")
@click.option("--package-name")
@click.option("--package-version")
@click.option("--template-name")
@click.option("--body")
def create_template_package_workingcopy(
    package_name, package_version, template_name, body
):
    if package_name is None:
        print("--package-name required")
        raise click.Abort()
    if package_version is None:
        print("--package-version required")
        raise click.Abort()
    if template_name is None:
        print("--template-name required")
        raise click.Abort()
    if body is None:
        print("--body required")
        raise click.Abort()
    file = open(body, "r")
    file_body = file.read()
    file.close()
    client = Client()
    response = client.post(
        "/rest/templates/packages/"
        + package_name
        + "/"
        + package_version
        + "/workingcopy/templates/"
        + template_name,
        body=file_body,
    )
    utils.pretty_print(response)


@click.command("delete-template-package-release")
@click.option("--package-name")
@click.option("--package-version")
def delete_template_package_release(package_name, package_version):
    if package_name is None:
        print("--package-name required")
        raise click.Abort()
    if package_version is None:
        print("--package-version required")
        raise click.Abort()
    client = Client()
    response = client.delete(
        "/rest/templates/packages/" + package_name + "/" + package_version + "/release"
    )
    utils.pretty_print(response)


@click.command("delete-template-package-workingcopy")
@click.option("--package-name")
@click.option("--package-version")
def delete_template_package_workingcopy(package_name, package_version):
    if package_name is None:
        print("--package-name required")
        raise click.Abort()
    if package_version is None:
        print("--package-version required")
        raise click.Abort()
    client = Client()
    response = client.delete(
        "/rest/templates/packages/"
        + package_name
        + "/"
        + package_version
        + "/workingcopy"
    )
    utils.pretty_print(response)


@click.command("get-template-package-release")
@click.option("--package-name")
@click.option("--package-version")
@click.option("--template-name")
def get_template_package_release(package_name, package_version, template_name):
    if package_name is None:
        print("--package-name required")
        raise click.Abort()
    if package_version is None:
        print("--package-version required")
        raise click.Abort()
    if template_name is None:
        print("--template-name required")
        raise click.Abort()
    client = Client()
    response = client.get(
        "/rest/templates/packages/"
        + package_name
        + "/"
        + package_version
        + "/release/templates/"
        + template_name
    )
    utils.pretty_print(response)


@click.command("get-template-package-release-model")
@click.option("--package-name")
@click.option("--package-version")
def get_template_package_release_model(package_name, package_version):
    if package_name is None:
        print("--package-name required")
        raise click.Abort()
    if package_version is None:
        print("--package-version required")
        raise click.Abort()
    client = Client()
    response = client.get(
        "/rest/templates/packages/"
        + package_name
        + "/"
        + package_version
        + "/release/model"
    )
    utils.pretty_print(response)


@click.command("get-template-package-workingcopy")
@click.option("--package-name")
@click.option("--package-version")
@click.option("--template-name")
def get_template_package_workingcopy(package_name, package_version, template_name):
    if package_name is None:
        print("--package-name required")
        raise click.Abort()
    if package_version is None:
        print("--package-version required")
        raise click.Abort()
    if template_name is None:
        print("--template-name required")
        raise click.Abort()
    client = Client()
    response = client.get(
        "/rest/templates/packages/"
        + package_name
        + "/"
        + package_version
        + "/workingcopy/templates/"
        + template_name
    )
    utils.pretty_print(response)


@click.command("get-template-package-workingcopy-model")
@click.option("--package-name")
@click.option("--package-version")
def get_template_package_workingcopy_model(package_name, package_version):
    if package_name is None:
        print("--package-name required")
        raise click.Abort()
    if package_version is None:
        print("--package-version required")
        raise click.Abort()
    client = Client()
    response = client.get(
        "/rest/templates/packages/"
        + package_name
        + "/"
        + package_version
        + "/workingcopy/model"
    )
    utils.pretty_print(response)


@click.command("get-templates-packages-release")
@click.option("--package-name")
@click.option("--package-version")
def get_templates_packages_release(package_name, package_version):
    if package_name is None:
        print("--package-name required")
        raise click.Abort()
    if package_version is None:
        print("--package-version required")
        raise click.Abort()
    client = Client()
    response = client.get(
        "/rest/templates/packages/"
        + package_name
        + "/"
        + package_version
        + "/release/templates"
    )
    utils.pretty_print(response)


@click.command("get-templates-packages-workingcopy")
@click.option("--package-name")
@click.option("--package-version")
def get_templates_packages_workingcopy(package_name, package_version):
    if package_name is None:
        print("--package-name required")
        raise click.Abort()
    if package_version is None:
        print("--package-version required")
        raise click.Abort()
    client = Client()
    response = client.get(
        "/rest/templates/packages/"
        + package_name
        + "/"
        + package_version
        + "/workingcopy/templates"
    )
    utils.pretty_print(response)


@click.command("perform-search-templates-packages")
@click.option("--terms")
def perform_search_templates_packages(terms):
    params = {}
    if terms is None:
        print("--terms required")
        raise click.Abort()
    params["terms"] = terms
    client = Client()
    response = client.post("/rest/templates/packages/perform_search", params=params)
    utils.pretty_print(response)


@click.command("update-template-package-workingcopy")
@click.option("--package-name")
@click.option("--package-version")
@click.option("--template-name")
@click.option("--body")
def update_template_package_workingcopy(
    package_name, package_version, template_name, body
):
    if package_name is None:
        print("--package-name required")
        raise click.Abort()
    if package_version is None:
        print("--package-version required")
        raise click.Abort()
    if template_name is None:
        print("--template-name required")
        raise click.Abort()
    if body is None:
        print("--body required")
        raise click.Abort()
    file = open(body, "r")
    file_body = file.read()
    file.close()
    client = Client()
    response = client.put(
        "/rest/templates/packages/"
        + package_name
        + "/"
        + package_version
        + "/workingcopy/templates/"
        + template_name,
        body=file_body,
    )
    utils.pretty_print(response)
