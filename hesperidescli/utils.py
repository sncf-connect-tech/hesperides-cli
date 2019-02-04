import json

from click import secho


def pretty_print(response):
    if 400 <= response.status_code < 600:
        secho('HTTP: {}'.format(response.status_code), fg='red')
    try:
        print(json.dumps(response.json(), indent=4, sort_keys=True))
    except TypeError:
        print("Error: " + response.content.decode("UTF-8"))
