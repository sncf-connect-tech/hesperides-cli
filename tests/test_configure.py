from click.testing import CliRunner
import unittest

from hesperidescli.configure.configure import delete_profile, set_profile


class TestConfigure(unittest.TestCase):
    def test_delete_profile_missing_profile_name(self):
        runner = CliRunner()
        result = runner.invoke(delete_profile)
        assert result.exit_code == 1
        assert result.output == "--profile_name required\nAborted!\n"

    def test_set_profile_missing_profile_name(self):
        runner = CliRunner()
        result = runner.invoke(set_profile)
        assert result.exit_code == 1
        assert result.output == "--profile_name required\nAborted!\n"
