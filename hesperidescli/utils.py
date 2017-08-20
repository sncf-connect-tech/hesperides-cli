import json


def pretty_print(response):
    if response:
        response_data = response.read()
        parsed_response_data = json.loads(response_data)
        # in case of exception remove stacktrace element from hesperides response because it's too large to display
        if 'stacktrace' in parsed_response_data:
            del parsed_response_data['stacktrace']
        print(json.dumps(parsed_response_data, indent=4, sort_keys=True))
