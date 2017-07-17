import http.client
import ssl
import urllib.parse
from hesperidescli.configure import configure


class Client:
    def __init__(self):
        endpoint = configure.get_config('endpoint')
        port = configure.get_config('port')
        protocol = configure.get_config('protocol')
        auth = configure.get_config('auth')
        self.headers = {
            'Accept': 'application/json',
            'Authorization': 'Basic %s' % auth,
            'Content-Type': 'application/json; charset=utf-8'
        }
        if protocol == 'http':
            self.connection = http.client.HTTPConnection(endpoint, port)
        else:
            self.connection = http.client.HTTPSConnection(endpoint, port, context=ssl._create_unverified_context())

    def get(self, path, params=None):
        return self._check_for_params('GET', path, params)

    def delete(self, path, params=None):
        return self._check_for_params('DELETE', path, params)

    def post(self, path, body=None):
        return self._call_with_body('POST', path, body)

    def put(self, path, body=None):
        return self._check_for_params('PUT', path, body)

    def _check_for_params(self, verb, path, params):
        if params is None:
            return self._call(verb, path)
        else:
            return self._call_with_params(verb, path, params)

    def _call(self, verb, path):
        self.connection.request(verb, path, headers=self.headers)
        response = self.connection.getresponse()
        return response

    def _call_with_body(self, verb, path, body):
        self.connection.request(verb, path, body, headers=self.headers)
        response = self.connection.getresponse()
        return response

    def _call_with_params(self, verb, path, params):
        params = urllib.parse.urlencode(params)
        self.connection.request(verb, path, params, headers=self.headers)
        response = self.connection.getresponse()
        return response
