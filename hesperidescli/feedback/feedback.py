# pylint: disable=unused-argument
import click


@click.command("post-feedback", deprecated=True)
@click.option("--message")
@click.option("--note")
def post_feedback(message, note):
    return
