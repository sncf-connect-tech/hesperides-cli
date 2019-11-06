import click
import pytest

from hesperidescli.client import Client

from .test_utils import init_client_config, setup_function, teardown_function


def test_create_client_fail_noconfig():
    with pytest.raises(click.UsageError) as excinfo:
        Client()
    assert (
        str(excinfo.value)
        == 'No profile has been configured. Please type "hesperides set-conf"'
    )


def test_create_client_succeed():
    init_client_config()
    Client()
