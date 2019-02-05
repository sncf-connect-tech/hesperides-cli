import io
import sys

import click

from hesperidescli.local.descriptor_utils import list_generated_files_contents


@click.command("local-validate-files")
@click.argument("descriptor-filepath")
def validate(descriptor_filepath):
    non_matching_pairs = 0
    for (
        template_filename,
        generated_filename,
        generated_content,
    ) in list_generated_files_contents(descriptor_filepath):
        with io.open(generated_filename, "r", encoding="utf-8") as generated_file:
            current_content = generated_file.read()
            if current_content == generated_content:
                click.secho("OK: {}".format(generated_filename))
            else:
                click.secho(
                    "!!! Le fichier local {} ne correspond pas au template {} avec les valeurs renseignées".format(
                        generated_filename, template_filename
                    ),
                    fg="red",
                )
                non_matching_pairs += 1
    if non_matching_pairs:
        sys.exit(1)
