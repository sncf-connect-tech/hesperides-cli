import click

from hesperidescli import utils
from hesperidescli.client import Client


@click.command('create-module')
@click.option('--from_module_name')
@click.option('--from_module_version')
@click.option('--from_is_working_copy', is_flag=True)
@click.option('--body')
def create_module(from_module_name, from_module_version, from_is_working_copy, body):
    if from_module_name is None and from_module_version:
        print('--from_module_name required when --from_module_version is given')
        return ''
    if from_module_name and from_module_version is None:
        print('--from_module_version required when --from_module_name is given')
        return ''
    if body is None:
        print('--body required')
        return ''
    file = open(body, "r")
    file_body = file.read()
    file.close()
    client = Client()
    if from_module_name and from_module_version:
        response = client.post('/rest/modules/?from_is_working_copy=' + str(
            from_is_working_copy) + '&from_module_name=' + from_module_name + '&from_module_version='
                               + from_module_version, file_body)
        utils.pretty_print(response)
    else:
        response = client.post('/rest/modules/', file_body)
        utils.pretty_print(response)


@click.command('create-module-release')
@click.option('--module_name')
@click.option('--module_version')
@click.option('--release_version')
def create_module_release(module_name, module_version, release_version):
    if module_name is None:
        print('--module_name required')
        return ''
    if module_version is None:
        print('--module_version required')
        return ''
    client = Client()
    if release_version:
        response = client.post(
            '/rest/modules/create_release?module_name=' + module_name + '&module_version=' + module_version
            + '&release_version=' + release_version)
        utils.pretty_print(response)
    else:
        response = client.post(
            '/rest/modules/create_release?module_name=' + module_name + '&module_version=' + module_version)
        utils.pretty_print(response)


@click.command('delete-module-workingcopy-template')
@click.option('--module_name')
@click.option('--module_version')
@click.option('--body')
def create_module_workingcopy_template(module_name, module_version, body):
    if module_name is None:
        print('--module_name required')
        return ''
    if module_version is None:
        print('--module_version required')
        return ''
    if body is None:
        print('--body required')
        return ''
    file = open(body, "r")
    file_body = file.read()
    file.close()
    client = Client()
    response = client.post('/rest/rest/modules' + module_name + '/' + module_version + '/workingcopy', file_body)
    utils.pretty_print(response)


@click.command('delete-module-release')
@click.option('--module_name')
@click.option('--module_version')
def delete_module_release(module_name, module_version):
    if module_name is None:
        print('--module_name required')
        return ''
    if module_version is None:
        print('--module_version required')
        return ''
    client = Client()
    response = client.delete('/rest/rest/modules' + module_name + '/' + module_version + '/release')
    utils.pretty_print(response)


@click.command('delete-module-workingcopy')
@click.option('--module_name')
@click.option('--module_version')
def delete_module_workingcopy(module_name, module_version):
    if module_name is None:
        print('--module_name required')
        return ''
    if module_version is None:
        print('--module_version required')
        return ''
    client = Client()
    response = client.delete('/rest/rest/modules' + module_name + '/' + module_version + '/workingcopy')
    utils.pretty_print(response)


@click.command('delete-module-workingcopy-template')
@click.option('--module_name')
@click.option('--module_version')
@click.option('--template_name')
def delete_module_workingcopy_template(module_name, module_version, template_name):
    if module_name is None:
        print('--module_name required')
        return ''
    if module_version is None:
        print('--module_version required')
        return ''
    if template_name is None:
        print('--template_name required')
        return ''
    client = Client()
    response = client.delete(
        '/rest/rest/modules' + module_name + '/' + module_version + '/workingcopy/templates/' + template_name)
    utils.pretty_print(response)


@click.command('get-module')
@click.option('--module_name')
@click.option('--module_version')
@click.option('--module_type')
def get_module(module_name, module_version, module_type):
    if module_name is None:
        print('--module_name required')
        return ''
    if module_type and module_version is None:
        print('--module_version required')
        return ''
    client = Client()
    if module_type is None and module_version is None:
        response = client.get('/rest/modules/' + module_name)
        utils.pretty_print(response)
    if module_type and module_version is None:
        response = client.get('/rest/modules/' + module_name + '/' + module_type)
        utils.pretty_print(response)
    if module_type and module_version:
        response = client.get('/rest/modules/' + module_name + '/' + module_type + '/' + module_version)
        utils.pretty_print(response)


@click.command('get-module-release')
@click.option('--module_name')
@click.option('--module_version')
def get_module_release(module_name, module_version):
    if module_name is None:
        print('--module_name required')
        return ''
    if module_version is None:
        print('--module_version required')
        return ''
    client = Client()
    response = client.get('/rest/modules/' + module_name + '/' + module_version + '/release')
    utils.pretty_print(response)


@click.command('get-module-release-template')
@click.option('--module_name')
@click.option('--module_version')
@click.option('--template_name')
def get_module_release_template(module_name, module_version, template_name):
    if module_name is None:
        print('--module_name required')
        return ''
    if module_version is None:
        print('--module_version required')
        return ''
    client = Client()
    response = client.get('/rest/modules/' + module_name + '/' + module_version + '/release/templates' + template_name)
    utils.pretty_print(response)


@click.command('get-module-release-templates')
@click.option('--module_name')
@click.option('--module_version')
def get_module_release_templates(module_name, module_version):
    if module_name is None:
        print('--module_name required')
        return ''
    if module_version is None:
        print('--module_version required')
        return ''
    client = Client()
    response = client.get('/rest/modules/' + module_name + '/' + module_version + '/release/templates')
    utils.pretty_print(response)


@click.command('get-module-workingcopy')
@click.option('--module_name')
@click.option('--module_version')
def get_module_workingcopy(module_name, module_version):
    if module_name is None:
        print('--module_name required')
        return ''
    if module_version is None:
        print('--module_version required')
        return ''
    client = Client()
    response = client.get('/rest/modules/' + module_name + '/' + module_version + '/workingcopy')
    utils.pretty_print(response)


@click.command('get-module-workingcopy-template')
@click.option('--module_name')
@click.option('--module_version')
@click.option('--template_name')
def get_module_workingcopy_template(module_name, module_version, template_name):
    if module_name is None:
        print('--module_name required')
        return ''
    if module_version is None:
        print('--module_version required')
        return ''
    if template_name is None:
        print('--template_name required')
        return ''
    client = Client()
    response = client.get(
        '/rest/modules/' + module_name + '/' + module_version + '/workingcopy/templates/' + template_name)
    utils.pretty_print(response)


@click.command('get-module-workingcopy-templates')
@click.option('--module_name')
@click.option('--module_version')
def get_module_workingcopy_templates(module_name, module_version):
    if module_name is None:
        print('--module_name required')
        return ''
    if module_version is None:
        print('--module_version required')
        return ''
    client = Client()
    response = client.get('/rest/modules/' + module_name + '/' + module_version + '/workingcopy/templates/')
    utils.pretty_print(response)


@click.command('get-modules')
def get_modules():
    client = Client()
    response = client.get('/rest/modules/')
    utils.pretty_print(response)


@click.command('perform-search-modules')
@click.option('--terms')
def perform_search_modules(terms):
    if terms is None:
        print('--terms required')
        return ''
    client = Client()
    response = client.post('/rest/modules/perform_search?terms=' + terms)
    utils.pretty_print(response)


@click.command('search-module')
@click.option('--terms')
def search_module(terms):
    params = {}
    if terms is None:
        print('--terms required')
        return ''
    else:
        params['terms'] = terms
    client = Client()
    response = client.post('/rest/modules/search', params)
    utils.pretty_print(response)


@click.command('update-module')
@click.option('--body')
def update_module(body):
    if body is None:
        print('--body required')
        return ''
    file = open(body, "r")
    file_body = file.read()
    file.close()
    client = Client()
    response = client.put('/rest/modules/', file_body)
    utils.pretty_print(response)


@click.command('update-module-workingcopy-template')
@click.option('--module_name')
@click.option('--module_version')
@click.option('--body')
def update_module_workingcopy_template(module_name, module_version, body):
    if module_name is None:
        print('--module_name required')
        return ''
    if module_version is None:
        print('--module_version required')
        return ''
    if body is None:
        print('--body required')
        return ''
    file = open(body, "r")
    file_body = file.read()
    file.close()
    client = Client()
    response = client.put('/rest/modules/' + module_name + '/' + module_version + '/workingcopy/templates', file_body)
    utils.pretty_print(response)
