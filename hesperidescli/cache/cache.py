import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command("delete-application-cache")
@click.option("--application-name")
@click.option("--platform-name")
def delete_application_cache(application_name, platform_name):
    if application_name is None:
        print("--application-name required")
        raise click.Abort()
    if platform_name is None:
        print("--platform-name required")
        raise click.Abort()
    client = Client()
    response = client.delete(
        "/rest/cache/application/" + application_name + "/" + platform_name
    )
    utils.pretty_print(response)


@click.command("delete-applications-cache")
def delete_applications_cache():
    client = Client()
    response = client.delete("/rest/cache/applications")
    utils.pretty_print(response)


@click.command("delete-modules-cache")
def delete_modules_cache():
    client = Client()
    response = client.delete("/rest/cache/modules")
    utils.pretty_print(response)


@click.command("delete-release-modules-cache")
@click.option("--module-name")
@click.option("--module-version")
def delete_release_module_cache(module_name, module_version):
    if module_name is None:
        print("--module-name required")
        raise click.Abort()
    if module_version is None:
        print("--module-version required")
        raise click.Abort()
    client = Client()
    response = client.delete(
        "/rest/cache/module/" + module_name + "/" + module_version + "/release"
    )
    utils.pretty_print(response)


@click.command("delete-template-package-cache")
@click.option("--template-name")
@click.option("--template-version")
def delete_release_template_package_cache(template_name, template_version):
    if template_name is None:
        print("--template-name required")
        raise click.Abort()
    if template_version is None:
        print("--template-version required")
        raise click.Abort()
    client = Client()
    response = client.delete(
        "/rest/cache/template/package/"
        + template_name
        + "/"
        + template_version
        + "/release"
    )
    utils.pretty_print(response)


@click.command("delete-templates-packages-cache")
def delete_templates_packages_cache():
    client = Client()
    response = client.delete("/rest/cache/templates/packages")
    utils.pretty_print(response)


@click.command("delete-workingcopy-modules-cache")
@click.option("--module-name")
@click.option("--module-version")
def delete_workingcopy_module_cache(module_name, module_version):
    if module_name is None:
        print("--module-name required")
        raise click.Abort()
    if module_version is None:
        print("--module-version required")
        raise click.Abort()
    client = Client()
    response = client.delete(
        "/rest/cache/module/" + module_name + "/" + module_version + "/workingcopy"
    )
    utils.pretty_print(response)


@click.command("delete-workingcopy-template-package-cache")
@click.option("--template-name")
@click.option("--template-version")
def delete_workingcopy_template_package_cache(template_name, template_version):
    if template_name is None:
        print("--template-name required")
        raise click.Abort()
    if template_version is None:
        print("--template-version required")
        raise click.Abort()
    client = Client()
    response = client.delete(
        "/rest/cache/template/package/"
        + template_name
        + "/"
        + template_version
        + "/workingcopy"
    )
    utils.pretty_print(response)


@click.command("regenerate-application-cache")
@click.option("--application-name")
@click.option("--platform-name")
def regenerate_application_cache(application_name, platform_name):
    if application_name is None:
        print("--application-name required")
        raise click.Abort()
    if platform_name is None:
        print("--platform-name required")
        raise click.Abort()
    client = Client()
    response = client.post(
        "/rest/cache/application/"
        + application_name
        + "/"
        + platform_name
        + "/regenerate"
    )
    utils.pretty_print(response)


@click.command("regenerate-module-cache")
@click.option("--module-name")
@click.option("--module-version")
def regenerate_module_cache(module_name, module_version):
    if module_name is None:
        print("--module-name required")
        raise click.Abort()
    if module_version is None:
        print("--module-version required")
        raise click.Abort()
    client = Client()
    response = client.post(
        "/rest/cache/module/" + module_name + "/" + module_version + "/regenerate"
    )
    utils.pretty_print(response)


@click.command("regenerate-template-package-cache")
@click.option("--template-name")
@click.option("--template-version")
def regenerate_template_package_cache(template_name, template_version):
    if template_name is None:
        print("--template-name required")
        raise click.Abort()
    if template_version is None:
        print("--template-version required")
        raise click.Abort()
    client = Client()
    response = client.post(
        "/rest/template/package/"
        + template_name
        + "/"
        + template_version
        + "/regenerate"
    )
    utils.pretty_print(response)
