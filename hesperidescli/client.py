import click
import requests
import urllib3

from hesperidescli.configure import configure


WARN_HEADERS = ("Deprecation", "Link", "Sunset")


class Client:
    def __init__(self):
        self.endpoint = configure.get_config("endpoint")
        auth = configure.get_credentials("auth")
        if configure.get_config("ignore_ssl_warnings", default=False) == "True":
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.headers = {
            "Accept": "application/json",
            "Authorization": "Basic %s" % auth,
            "Content-Type": "application/json; charset=utf-8",
        }

    def get(self, path, params=None, accept=None):
        headers = self.headers.copy()
        if accept:
            headers["Accept"] = accept
        return _handle_warnings(
            requests.get(
                self.endpoint + path, params=params, headers=headers, verify=False
            )
        )

    def delete(self, path, params=None):
        return _handle_warnings(
            requests.delete(
                self.endpoint + path, params=params, headers=self.headers, verify=False
            )
        )

    def post(self, path, params=None, body=None):
        if body:
            return _handle_warnings(
                requests.post(
                    self.endpoint + path,
                    params=params,
                    data=body,
                    headers=self.headers,
                    verify=False,
                )
            )
        return _handle_warnings(
            requests.post(
                self.endpoint + path,
                params=params,
                headers=self.headers,
                verify=False,
                stream=True,
            )
        )

    def put(self, path, params=None, body=None):
        if body:
            return _handle_warnings(
                requests.put(
                    self.endpoint + path,
                    params=params,
                    data=body,
                    headers=self.headers,
                    verify=False,
                )
            )
        return _handle_warnings(
            requests.put(
                self.endpoint + path, params=params, headers=self.headers, verify=False
            )
        )


def _handle_warnings(resp):
    for warn_header in WARN_HEADERS:
        if warn_header in resp.headers:
            click.secho(
                "{}: {}".format(warn_header, resp.headers[warn_header]), fg="yellow"
            )
    return resp
