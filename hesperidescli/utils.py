import json


def pretty_print(response):
    if response:
        data = response.read()
        parsed = json.loads(data)
        if parsed['stacktrace'] is None:
            print(json.dumps(parsed, indent=4, sort_keys=True))
        else:
            # in case of exception remove stacktrace element from hesperides response because it's too large to display
            del parsed['stacktrace']
            print(json.dumps(parsed, indent=4, sort_keys=True))
