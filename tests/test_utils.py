from contextlib import contextmanager
from os.path import isdir
from shutil import move, rmtree

from click.testing import CliRunner
from httmock import all_requests, HTTMock

from hesperidescli.configure import set_conf, set_profile
from hesperidescli.configure.configfile import ConfigFile


_BACKUP_DIR = None


def setup_function():
    global _BACKUP_DIR
    # backup any existing ~/hesperides directory
    if not _BACKUP_DIR and isdir(ConfigFile._CONFIG_DIR):
        _BACKUP_DIR = ConfigFile._CONFIG_DIR + ".bak"
        move(ConfigFile._CONFIG_DIR, _BACKUP_DIR)


def teardown_function():
    global _BACKUP_DIR
    # restore ~/hesperides pre-existing directory
    if _BACKUP_DIR:
        rmtree(ConfigFile._CONFIG_DIR, ignore_errors=True)
        move(_BACKUP_DIR, ConfigFile._CONFIG_DIR)
        _BACKUP_DIR = None


def init_client_config():
    result = CliRunner().invoke(
        set_conf,
        [
            "--profile",
            "default",
            "--username",
            "user",
            "--password",
            "password",
            "--hesperides-endpoint",
            "http://localhost:8888",
        ],
    )
    assert result.exit_code == 0, result.output
    result = CliRunner().invoke(set_profile, ["--profile-name", "default"])
    assert result.exit_code == 0, result.output


@contextmanager
def mock_server(content, status_code=200):
    @all_requests
    def match_all(url, request):
        return {'status_code': status_code,
                'content': content}
    with HTTMock(match_all):
        yield
