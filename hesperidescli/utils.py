import json


def prettyprint(response):
    if response:
        data = response.read()
        parsed = json.loads(data)
        print(json.dumps(parsed, indent=4, sort_keys=True))
