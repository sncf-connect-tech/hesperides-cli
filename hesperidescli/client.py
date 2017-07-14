import http.client
import urllib.parse
from hesperidescli.configure import commands


class Client:
    def __init__(self):
        endpoint = commands.get_config('endpoint')
        port = commands.get_config('port')
        protocol = commands.get_config('protocal')
        if protocol == 'http':
            self.connection = http.client.HTTPConnection(endpoint, port)
        else:
            self.connection = http.client.HTTPSConnection(endpoint, port)

    def call(self, path):
        self.connection.request("GET", path)
        response = self.connection.getresponse()
        return response

    def call(self, path, params):
        params = urllib.parse.urlencode(params)
        self.connection.request("GET", path, params)
        response = self.connection.getresponse()
        return response
