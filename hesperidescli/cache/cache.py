# pylint: disable=unused-argument
import click


@click.command("delete-application-cache", deprecated=True)
@click.option("--application-name")
@click.option("--platform-name")
def delete_application_cache(application_name, platform_name):
    return


@click.command("delete-applications-cache", deprecated=True)
def delete_applications_cache():
    return


@click.command("delete-modules-cache", deprecated=True)
def delete_modules_cache():
    return


@click.command("delete-release-modules-cache", deprecated=True)
@click.option("--module-name")
@click.option("--module-version")
def delete_release_module_cache(module_name, module_version):
    return


@click.command("delete-template-package-cache", deprecated=True)
@click.option("--template-name")
@click.option("--template-version")
def delete_release_template_package_cache(template_name, template_version):
    return


@click.command("delete-templates-packages-cache")
def delete_templates_packages_cache():
    return


@click.command("delete-workingcopy-modules-cache", deprecated=True)
@click.option("--module-name")
@click.option("--module-version")
def delete_workingcopy_module_cache(module_name, module_version):
    return


@click.command("delete-workingcopy-template-package-cache", deprecated=True)
@click.option("--template-name")
@click.option("--template-version")
def delete_workingcopy_template_package_cache(template_name, template_version):
    return


@click.command("regenerate-application-cache", deprecated=True)
@click.option("--application-name")
@click.option("--platform-name")
def regenerate_application_cache(application_name, platform_name):
    return


@click.command("regenerate-module-cache", deprecated=True)
@click.option("--module-name")
@click.option("--module-version")
def regenerate_module_cache(module_name, module_version):
    return


@click.command("regenerate-template-package-cache", deprecated=True)
@click.option("--template-name")
@click.option("--template-version")
def regenerate_template_package_cache(template_name, template_version):
    return
