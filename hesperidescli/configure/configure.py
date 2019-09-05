import base64, os

import click

from hesperidescli.configure.reader import ConfigFileReader, ConfigParserError
from hesperidescli.configure.writer import ConfigFileWriter


@click.command("delete-profile")
@click.argument("profile-name")
def delete_profile(profile_name):
    config_writer = ConfigFileWriter()
    config_writer.remove_config_section(profile_name)
    if ConfigFileReader().get_profile() == profile_name:
        config_writer.remove_profile()
    ConfigFileWriter().remove_credentials_section(profile_name)


@click.command("get-conf")
def get_conf():
    config_reader = ConfigFileReader()
    config_reader.print_config()
    config_reader.print_credentials()


@click.command("get-profile")
def get_profile():
    reader = ConfigFileReader()
    click.secho(reader.get_profile())


def get_config(key, **kwargs):
    config_reader = ConfigFileReader()
    try:
        return config_reader.get_config_item(config_reader.get_profile(), key, **kwargs)
    except ConfigParserError:
        return config_reader.get_config_item(key, **kwargs)


def get_credentials(key, **kwargs):
    config_reader = ConfigFileReader()
    try:
        return config_reader.get_credentials_item(
            config_reader.get_profile(), key, **kwargs
        )
    except ConfigParserError:
        return config_reader.get_credentials_item(key, **kwargs)


@click.command("set-conf")
@click.argument("profile-name", default="default")
@click.option(
    "--username",
    prompt=True,
    hide_input=False,
    confirmation_prompt=False,
    default=os.environ.get("USER", os.environ.get("USERNAME")),
)
@click.option(
    "--password", prompt=True, hide_input=True, confirmation_prompt=False, default=""
)
@click.option(
    "--hesperides-endpoint",
    prompt=True,
    hide_input=False,
    confirmation_prompt=False,
    default="https://hesperides",
)
@click.option(
    "--ignore-ssl-warnings",
    prompt=True,
    hide_input=False,
    confirmation_prompt=False,
    flag_value=True,
    default=False,
)
def set_conf(
    profile_name, username, password, hesperides_endpoint, ignore_ssl_warnings
):
    basic_auth = base64.b64encode(str.encode("%s:%s" % (username, password))).decode(
        "UTF-8"
    )
    config_writer = ConfigFileWriter()
    config_writer.update_config(
        profile_name,
        {
            "endpoint": hesperides_endpoint,
            "ignore_ssl_warnings": str(ignore_ssl_warnings),
        },
    )
    ConfigFileWriter().update_credentials(
        profile_name, {"username": username, "auth": basic_auth}
    )
    config_writer.update_config("config", {"profile": profile_name})


@click.command("use-profile")
@click.argument("profile-name")
def use_profile(profile_name):
    ConfigFileWriter().update_config("config", {"profile": profile_name})
