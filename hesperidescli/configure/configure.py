import click

from hesperidescli.configure.writer import ConfigFileWriter


@click.command('configure')
@click.option('--username', prompt=True, hide_input=False, confirmation_prompt=False)
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=False)
@click.option('--hesperides_endpoint', prompt=True, hide_input=False, confirmation_prompt=False)
def command(username, password, hesperides_endpoint):
    click.echo('Configure hesperides')
    print('username: ' + username)
    print('password: ' + password)
    print('hesperides_endpoint: ' + hesperides_endpoint)
    writer = ConfigFileWriter()
    writer.update_config('sfdf')
