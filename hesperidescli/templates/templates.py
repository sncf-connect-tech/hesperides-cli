import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.group('templates')
def command():
    pass


@click.group('packages', invoke_without_command=True)
@click.option('--package_name')
@click.option('--package_version')
@click.pass_context
def packages(ctx, package_name, package_version):
    if ctx.invoked_subcommand is None:
        client = Client()
        response = client.post('/rest/templates/packages/')
        utils.prettyprint(response)
    else:
        if package_name is None:
            print('--package_name required')
            return ''
        if package_version is None:
            print('--package_version required')
            return ''
        ctx['PACKAGE_NAME'] = package_name
        ctx['PACKAGE_VERSION'] = package_version


@click.group('release', invoke_without_command=True)
@click.pass_context
def packages_release(ctx):
    if ctx.invoked_subcommand is None:
        client = Client()
        response = client.delete(
            '/rest/templates/packages/' + ctx['PACKAGE_NAME'] + '/' + ctx[
                'PACKAGE_VERSION'] + '/release')
        utils.prettyprint(response)


@click.command('model')
@click.pass_context
def packages_release_model(ctx):
    client = Client()
    response = client.get(
        '/rest/templates/packages/' + ctx['PACKAGE_NAME'] + '/' + ctx[
            'PACKAGE_VERSION'] + '/release/model')
    utils.prettyprint(response)


@click.command('templates')
@click.option('--template_name')
@click.pass_context
def packages_release_templates(ctx, template_name):
    if template_name:
        client = Client()
        response = client.get(
            '/rest/templates/packages/' + ctx['PACKAGE_NAME'] + '/' + ctx[
                'PACKAGE_VERSION'] + '/release/templates/' + template_name)
        utils.prettyprint(response)
    else:
        client = Client()
        response = client.get(
            '/rest/templates/packages/' + ctx['PACKAGE_NAME'] + '/' + ctx['PACKAGE_VERSION'] + '/release/templates')
        utils.prettyprint(response)


@click.group('workingcopy', invoke_without_command=True)
@click.pass_context
def packages_workingcopy(ctx):
    client = Client()
    response = client.delete(
        '/rest/templates/packages/' + ctx['PACKAGE_NAME'] + '/' + ctx['PACKAGE_VERSION'] + '/workingcopy')
    utils.prettyprint(response)


@click.command('model')
@click.pass_context
def packages_workingcopy_model(ctx):
    client = Client()
    response = client.get(
        '/rest/templates/packages/' + ctx['PACKAGE_NAME'] + '/' + ctx['PACKAGE_VERSION'] + '/workingcopy/model')
    utils.prettyprint(response)


@click.command('templates')
@click.option('--templates_name')
@click.option('--delete', is_flag=True, default=False)
@click.option('--get', is_flag=True, default=False)
@click.option('--post', is_flag=True, default=False)
@click.option('--put', is_flag=True, default=False)
@click.pass_context
def packages_workingcopy_templates(ctx, template_name, delete, get, post, put):
    if template_name is None and delete or get:
        print('--template_name required')
        return ''

    if template_name is None and not delete and get and not post and not put:
        client = Client()
        response = client.get(
            '/rest/templates/packages/' + ctx['PACKAGE_NAME'] + '/' + ctx[
                'PACKAGE_VERSION'] + '/workingcopy/templates')
        utils.prettyprint(response)

    if template_name is None and not delete and not get and post and not put:
        client = Client()
        response = client.post(
            '/rest/templates/packages/' + ctx['PACKAGE_NAME'] + '/' + ctx[
                'PACKAGE_VERSION'] + '/workingcopy/templates')
        utils.prettyprint(response)

    if template_name is None and not delete and not get and not post and put:
        client = Client()
        response = client.put(
            '/rest/templates/packages/' + ctx['PACKAGE_NAME'] + '/' + ctx[
                'PACKAGE_VERSION'] + '/workingcopy/templates')
        utils.prettyprint(response)

    if template_name is not None and not delete and get and not post and not put:
        client = Client()
        response = client.get(
            '/rest/templates/packages/' + ctx['PACKAGE_NAME'] + '/' + ctx[
                'PACKAGE_VERSION'] + '/workingcopy/templates/' + template_name)
        utils.prettyprint(response)

    if template_name is not None and delete and not get and not post and not put:
        client = Client()
        response = client.delete(
            '/rest/templates/packages/' + ctx['PACKAGE_NAME'] + '/' + ctx[
                'PACKAGE_VERSION'] + '/workingcopy/templates/' + template_name)
        utils.prettyprint(response)


@click.command('create_release')
@click.option('--package_name')
@click.option('--package_version')
def packages_create_release(package_name, package_version):
    if package_name is None:
        package_name = ''
    if package_version is None:
        package_version = ''
    client = Client()
    response = client.post(
        '/rest/templates/packages/create_release?package_name=' + package_name + '&package_version=' + package_version)
    utils.prettyprint(response)


@click.command('perform_search')
@click.option('--term')
def packages_perform_search(term):
    if term is None:
        term = ''
    client = Client()
    response = client.post('/rest/templates/packages/perform_search?terms=' + term)
    utils.prettyprint(response)


command.add_command(packages)
packages.add_command(packages_release)
packages_release.add_command(packages_release_model)
packages_release.add_command(packages_release_templates)
packages.add_command(packages_workingcopy)
packages_workingcopy.add_command(packages_workingcopy_model)
packages_workingcopy.add_command(packages_workingcopy_templates)
packages.add_command(packages_create_release)
packages.add_command(packages_perform_search)
