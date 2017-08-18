import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command('create-templates-package-release')
@click.option('--from_package_name')
@click.option('--from_package_version')
@click.option('--body')
def create_templates_packages_release(from_package_name, from_package_version, from_is_working_copy, body):
    if from_package_name is None and from_package_version:
        print('--from_package_name required when --from_package_version is given')
        return ''
    if from_package_name and from_package_version is None:
        print('--from_package_version required when --from_package_name is given')
        return ''
    if body is None:
        print('--body required')
        return ''
    file = open(body, "r")
    file_body = file.read()
    file.close()
    client = Client()
    response = client.post(
        '/rest/templates/packages?from_package_name=' + from_package_name + '&from_package_version='
        + from_package_version, file_body)
    utils.pretty_print(response)


@click.command('create-templates-packages')
@click.option('--from_package_name')
@click.option('--from_package_version')
@click.option('--from_is_working_copy', is_flag=True)
@click.option('--body')
def create_templates_packages(from_package_name, from_package_version, from_is_working_copy, body):
    if from_package_name is None and from_package_version:
        print('--from_package_name required when --from_package_version is given')
        return ''
    if from_package_name and from_package_version is None:
        print('--from_package_version required when --from_package_name is given')
        return ''
    if body is None:
        print('--body required')
        return ''
    file = open(body, "r")
    file_body = file.read()
    file.close()
    client = Client()
    if from_package_name and from_package_version:
        response = client.post(
            '/rest/templates/packages?from_package_name=' + from_package_name + '&from_package_version='
            + from_package_version + '&from_is_working_copy=' + from_is_working_copy, file_body)
    else:
        response = client.post('/rest/templates/packages?from_is_working_copy=' + from_is_working_copy, file_body)
    utils.pretty_print(response)


@click.command('create-workingcopy-template')
@click.option('--package_name')
@click.option('--package_version')
@click.option('--template_name')
@click.option('--body')
def create_workingcopy_template(package_name, package_version, template_name, body):
    if package_name is None:
        print('--package_name required')
        return ''
    if package_version is None:
        print('--package_version required')
        return ''
    if template_name is None:
        print('--template_name required')
        return ''
    if body is None:
        print('--body required')
        return ''
    file = open(body, "r")
    file_body = file.read()
    file.close()
    client = Client()
    response = client.post(
        '/rest/templates/packages/' + package_name + '/' + package_version + '/workingcopy/templates/' + template_name,
        file_body)
    utils.pretty_print(response)


@click.command('delete-release-template-package')
@click.option('--package_name')
@click.option('--package_version')
def delete_release_template_package(package_name, package_version):
    if package_name is None:
        print('--package_name required')
        return ''
    if package_version is None:
        print('--package_version required')
        return ''
    client = Client()
    response = client.delete('/rest/templates/packages/' + package_name + '/' + package_version + '/release')
    utils.pretty_print(response)


@click.command('delete-workingcopy-template-package')
@click.option('--package_name')
@click.option('--package_version')
def delete_workingcopy_template_package(package_name, package_version):
    if package_name is None:
        print('--package_name required')
        return ''
    if package_version is None:
        print('--package_version required')
        return ''
    client = Client()
    response = client.delete('/rest/templates/packages/' + package_name + '/' + package_version + '/workingcopy')
    utils.pretty_print(response)


@click.command('get-release-templates')
@click.option('--package_name')
@click.option('--package_version')
def get_release_templates(package_name, package_version):
    if package_name is None:
        print('--package_name required')
        return ''
    if package_version is None:
        print('--package_version required')
        return ''
    client = Client()
    response = client.get('/rest/templates/packages/' + package_name + '/' + package_version + '/release/templates')
    utils.pretty_print(response)


@click.command('get-release-template')
@click.option('--package_name')
@click.option('--package_version')
@click.option('--template_name')
def get_release_template(package_name, package_version, template_name):
    if package_name is None:
        print('--package_name required')
        return ''
    if package_version is None:
        print('--package_version required')
        return ''
    if template_name is None:
        print('--template_name required')
        return ''
    client = Client()
    response = client.get(
        '/rest/templates/packages/' + package_name + '/' + package_version + '/release/templates/' + template_name)
    utils.pretty_print(response)


@click.command('get-template-package-release-model')
@click.option('--package_name')
@click.option('--package_version')
def get_template_package_release_model(package_name, package_version):
    if package_name is None:
        print('--package_name required')
        return ''
    if package_version is None:
        print('--package_version required')
        return ''
    client = Client()
    response = client.get('/rest/templates/packages/' + package_name + '/' + package_version + '/release/model')
    utils.pretty_print(response)


@click.command('get-template-package-workingcopy-model')
@click.option('--package_name')
@click.option('--package_version')
def get_template_package_workingcopy_model(package_name, package_version):
    if package_name is None:
        print('--package_name required')
        return ''
    if package_version is None:
        print('--package_version required')
        return ''
    client = Client()
    response = client.get('/rest/templates/packages/' + package_name + '/' + package_version + '/workingcopy/model')
    utils.pretty_print(response)


@click.command('get-workingcopy-templates')
@click.option('--package_name')
@click.option('--package_version')
def get_workingcopy_templates(package_name, package_version):
    if package_name is None:
        print('--package_name required')
        return ''
    if package_version is None:
        print('--package_version required')
        return ''
    client = Client()
    response = client.get('/rest/templates/packages/' + package_name + '/' + package_version + '/workingcopy/templates')
    utils.pretty_print(response)


@click.command('get-workingcopy-template')
@click.option('--package_name')
@click.option('--package_version')
@click.option('--template_name')
def get_workingcopy_template(package_name, package_version, template_name):
    if package_name is None:
        print('--package_name required')
        return ''
    if package_version is None:
        print('--package_version required')
        return ''
    if template_name is None:
        print('--template_name required')
        return ''
    client = Client()
    response = client.get(
        '/rest/templates/packages/' + package_name + '/' + package_version + '/workingcopy/templates/' + template_name)
    utils.pretty_print(response)


@click.command('templates-packages-perform-search')
@click.option('--terms')
def templates_packages_perform_search(terms):
    if terms is None:
        print('--terms required')
        return ''
    client = Client()
    response = client.get('/rest/templates/packages/perform_search?terms=' + terms)
    utils.pretty_print(response)


@click.command('update-workingcopy-template')
@click.option('--package_name')
@click.option('--package_version')
@click.option('--template_name')
@click.option('--body')
def update_workingcopy_template(package_name, package_version, template_name, body):
    if package_name is None:
        print('--package_name required')
        return ''
    if package_version is None:
        print('--package_version required')
        return ''
    if template_name is None:
        print('--template_name required')
        return ''
    if body is None:
        print('--body required')
        return ''
    file = open(body, "r")
    file_body = file.read()
    file.close()
    client = Client()
    response = client.put(
        '/rest/templates/packages/' + package_name + '/' + package_version + '/workingcopy/templates/' + template_name,
        file_body)
    utils.pretty_print(response)
