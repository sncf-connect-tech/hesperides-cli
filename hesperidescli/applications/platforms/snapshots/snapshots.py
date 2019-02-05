# pylint: disable=unused-argument
import click


@click.command("get-application-platform-snapshots", deprecated=True)
@click.option("--application-name")
@click.option("--platform-name")
def get_application_platform_snapshots(application_name, platform_name):
    return


@click.command("restore-application-platform-snapshots", deprecated=True)
@click.option("--application-name")
@click.option("--platform-name")
def restore_application_platform_snapshots(application_name, platform_name):
    return


@click.command("take-application-platform-snapshot", deprecated=True)
@click.option("--application-name")
@click.option("--platform-name")
@click.option("--body")
def take_application_platform_snapshot(application_name, platform_name, body):
    return
