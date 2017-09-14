import json


def pretty_print(response):
    try:
        print(json.dumps(response.json(), indent=4, sort_keys=True))
    except TypeError:
        print("Error: " + response.content.decode('UTF-8'))
