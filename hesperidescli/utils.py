import json, sys

from click import secho, Option, Parameter


def pretty_print(response):
    if 400 <= response.status_code < 600:
        secho("HTTP: {}".format(response.status_code), fg="red")
    try:
        secho(json.dumps(response.json(), indent=4, sort_keys=True))
    except (TypeError, json.decoder.JSONDecodeError):
        secho("Error: " + response.content.decode("UTF-8"), fg="red")


class LazyPromptOption(Option):
    'Only prompt for a value if zero CLI arguments have been provided'
    def full_process_value(self, ctx, value):
        assert self.prompt
        if len(sys.argv) > 2:  # we bypass the default behaviour and force CLI args processing:
            return Parameter.full_process_value(self, ctx, value)
        # default behaviour:
        return super().full_process_value(ctx, value)
