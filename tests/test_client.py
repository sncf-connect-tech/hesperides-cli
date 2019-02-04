import pytest

from hesperidescli.client import Client

from .test_utils import init_client_config, setup_function, teardown_function


def test_create_client_fail_noconfig():
    with pytest.raises(SystemExit):
        Client()


def test_create_client_succeed():
    init_client_config()
    Client()
