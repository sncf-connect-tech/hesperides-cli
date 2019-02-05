import io
import os
import shutil

import click

from hesperidescli.local.descriptor_utils import list_generated_files_contents


@click.command("local-generate-files")
@click.argument("descriptor-filepath")
def generate(descriptor_filepath):
    for (
        template_filename,
        generated_filename,
        generated_content,
    ) in list_generated_files_contents(descriptor_filepath):
        if os.path.exists(generated_filename):
            with io.open(generated_filename, "r", encoding="utf-8") as old_file:
                if old_file.read() != generated_content:
                    # We generate a backup
                    shutil.copyfile(generated_filename, generated_filename + ".bak")
        with io.open(generated_filename, "w", encoding="utf-8") as generated_file:
            click.secho(
                "GENERATION du fichier local {} à partir du template {}".format(
                    generated_filename, template_filename
                ),
                fg="red",
            )
            generated_file.write(generated_content)
