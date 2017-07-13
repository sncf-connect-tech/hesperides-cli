import http.client
import urllib.parse


class Client:
    def __init__(self):
        self.connection = http.client.HTTPConnection("localhost", 8080)

    def call(self, path):
        self.connection.request("GET", path)
        response = self.connection.getresponse()
        return response

    def call(self, path, params):
        params = urllib.parse.urlencode(params)
        self.connection.request("GET", path, params)
        response = self.connection.getresponse()
        return response
