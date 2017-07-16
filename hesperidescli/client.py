import http.client
import urllib.parse
from hesperidescli.configure import commands


class Client:
    def __init__(self):
        endpoint = commands.get_config('endpoint')
        port = commands.get_config('port')
        protocol = commands.get_config('protocol')
        if protocol == 'http':
            self.connection = http.client.HTTPConnection(endpoint, port)
        else:
            self.connection = http.client.HTTPSConnection(endpoint, port)

    def get(self, path, params=None):
        return self._check_for_params('GET', path, params)

    def delete(self, path, params=None):
        return self._check_for_params('DELETE', path, params)

    def post(self, path, params=None):
        return self._check_for_params('POST', path, params)

    def put(self, path, params=None):
        return self._check_for_params('PUT', path, params)

    def _check_for_params(self, verb, path, params):
        if params is None:
            return self._call(verb, path)
        else:
            return self._call_with_params(verb, path, params)

    def _call(self, verb, path):
        self.connection.request(verb, path)
        response = self.connection.getresponse()
        return response

    def _call_with_params(self, verb, path, params):
        params = urllib.parse.urlencode(params)
        self.connection.request(verb, path, params)
        response = self.connection.getresponse()
        return response
