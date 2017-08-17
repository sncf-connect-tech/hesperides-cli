import click
from hesperidescli.applications import applications
from hesperidescli.cache import cache
from hesperidescli.configure import configure
from hesperidescli.events import events
from hesperidescli.feedback import feedback
from hesperidescli.files import files
from hesperidescli.indexation import indexation
from hesperidescli.modules import modules
from hesperidescli.properties import properties
from hesperidescli.stats import stats
from hesperidescli.templates import templates
from hesperidescli.users import users
from hesperidescli.versions import versions


@click.group()
def cli():
    pass


cli.add_command(applications.get_application)
cli.add_command(applications.get_application_from_module)
cli.add_command(applications.perform_search)
cli.add_command(cache.command)
cli.add_command(configure.command)
cli.add_command(events.get_events)
cli.add_command(feedback.post_feedback)
cli.add_command(files.command)
cli.add_command(indexation.perform_reindex)
cli.add_command(modules.command)
cli.add_command(properties.get_global_properties)
cli.add_command(properties.get_global_properties_usage)
cli.add_command(properties.get_properties)
cli.add_command(properties.get_properties_instance_model)
cli.add_command(stats.get_stats)
cli.add_command(templates.command)
cli.add_command(users.get_user)
cli.add_command(versions.get_versions)
