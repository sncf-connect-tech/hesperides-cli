from click.testing import CliRunner
import unittest

from hesperidescli.configure import get_profile, set_conf, use_profile, delete_profile

from .test_utils import init_client_config


class TestConfigure(unittest.TestCase):
    def test_set_conf_ok(self):
        init_client_config()

    def test_set_conf_with_default_profile_name_ok(self):
        result = CliRunner().invoke(
            set_conf,
            [
                "--username",
                "user",
                "--password",
                "password",
                "--hesperides-endpoint",
                "http://localhost:8888",
            ],
        )
        assert result.exit_code == 0, result.output

    def test_get_profile_ok(self):
        init_client_config()
        result = CliRunner().invoke(get_profile)
        assert result.exit_code == 0, result.output
        assert result.output.strip() == "default"

    def test_use_profile_missing_profile_name(self):
        result = CliRunner().invoke(use_profile)
        assert result.exit_code == 2

    def test_delete_profile_missing_profile_name(self):
        init_client_config()
        result = CliRunner().invoke(delete_profile)
        assert result.exit_code == 2
