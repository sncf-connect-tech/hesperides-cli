import io
import json
from os import path
import re

COLOR_RED = "\033[31m"
COLOR_END = "\033[0m"

ITERABLE_MUSTACHE_PATTERN = re.compile(
    r" *{{ *#([^{}| ]+) *}} *\n(.*)\n *{{ */\1 *}} *\n", re.DOTALL
)
SINGLE_MUSTACHE_PATTERN = re.compile(r"{{ *([^{}| ]+) *\|? *(.*) *}}")
DEFAULT_ANNOTATION_PATTERN = re.compile(r'@default +(("(?:[^"\\]|\\.)+")|([^" ]+))')
PATTERN_ANNOTATION_PATTERN = re.compile(r'@pattern +(("(?:[^"\\]|\\.)+")|([^" ]+))')


def list_generated_files_contents(descriptor_filepath):
    with io.open(descriptor_filepath, "r", encoding="utf-8") as json_config_file:
        descriptor_config = json.load(json_config_file)
    for module_name, module_templates in sorted(descriptor_config.items()):
        for template_filepath, tpl_config in sorted(module_templates.items()):
            with io.open(template_filepath, "r", encoding="utf-8") as template_file:
                new_local_file_content = template_file.read()
            if "local" in tpl_config:
                for key in tpl_config.keys():
                    if key != "local" and key in tpl_config["local"]:
                        tpl_config[key] = tpl_config["local"][key]
                try:
                    new_local_file_content = substitute_all_mustaches(
                        new_local_file_content, tpl_config["local"].get("values", {})
                    )
                except ValueError as error:
                    error.args = (
                        error.args[0]
                        + " for template "
                        + template_filepath
                        + " in module "
                        + module_name,
                    )
                    raise
            yield template_filepath, path.join(
                tpl_config["location"], tpl_config["filename"]
            ), new_local_file_content


def substitute_all_mustaches(template_content, local_values):
    "Yes, alternatively we could use Jinja2 or Pybar to do this in a cleaner way"
    # pylint: disable=cell-var-from-loop
    def replace_iterable_mustache(match):
        iterable_name = match.group(1)
        subcontent = match.group(2)
        if iterable_name not in local_values:
            raise ValueError(
                COLOR_RED
                + "Aucune valeur n'a été définie pour l'itérable {}".format(
                    iterable_name
                )
                + COLOR_END
            )
        return "".join(
            re.sub(
                SINGLE_MUSTACHE_PATTERN,
                lambda match: replace_mustache_value(match, iter_values),
                subcontent,
            )
            + "\n"
            for iter_values in local_values[iterable_name]
        )

    template_content = re.sub(
        ITERABLE_MUSTACHE_PATTERN, replace_iterable_mustache, template_content
    )
    return re.sub(
        SINGLE_MUSTACHE_PATTERN,
        lambda match: replace_mustache_value(match, local_values),
        template_content,
    )


def replace_mustache_value(match, local_values):
    key = match.group(1)
    post_pipe = match.group(2)
    value = ""
    if key in local_values:
        value = str(local_values[key]) if local_values[key] is not None else "null"
        if isinstance(local_values[key], bool):
            value = "true" if local_values[key] else "false"
    elif (
        post_pipe and "@default" in post_pipe
    ):  # Check if a default value has been provided in the template with @default tag
        default_match = re.search(DEFAULT_ANNOTATION_PATTERN, post_pipe)
        if not default_match:
            raise ValueError(
                COLOR_RED
                + "Invalide @default pour la moustache {}".format(key)
                + COLOR_END
            )
        value = default_match.group(1)
        if value and value[0] == '"':
            value = value[1:-1].replace('\\"', '"')
    if not value and "@required" in post_pipe:
        raise ValueError(
            COLOR_RED
            + "Aucune valeur n'a été définie pour la moustache {}".format(key)
            + COLOR_END
        )
    if post_pipe and "@pattern" in post_pipe and (value or "@required" in post_pipe):
        pattern_match = re.search(PATTERN_ANNOTATION_PATTERN, post_pipe)
        if not pattern_match:
            raise ValueError(
                COLOR_RED
                + "Invalide @pattern pour la moustache {}".format(key)
                + COLOR_END
            )
        pattern = pattern_match.group(1)
        if pattern and pattern[0] == '"':
            pattern = pattern[1:-1]
        pattern = pattern.replace("\\\\", "\\")
        if not re.match(pattern, value):
            raise ValueError(
                COLOR_RED
                + "La valeur {} ne respecte pas le @pattern {}".format(value, pattern)
                + COLOR_END
            )
    return value
