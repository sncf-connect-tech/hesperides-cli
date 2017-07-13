import http.client


class Client:
    def __init__(self):
        self.connection = http.client.HTTPConnection("localhost", 8080)

    def call(self, path):
        self.connection.request("GET", path)
        response = self.connection.getresponse()
        return response
