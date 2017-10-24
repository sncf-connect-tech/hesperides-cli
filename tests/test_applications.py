from click.testing import CliRunner
import unittest

from hesperidescli.applications.applications import get_application, get_application_from_module, \
    perform_search_applications


class TestApplications(unittest.TestCase):
    def test_get_application_missing_application_name(self):
        runner = CliRunner()
        result = runner.invoke(get_application)
        assert result.exit_code == 1

    def test_get_application_from_module_missing_module(self):
        runner = CliRunner()
        result = runner.invoke(get_application_from_module)
        assert result.exit_code == 1

    def test_get_application_from_module_missing_version(self):
        runner = CliRunner()
        result = runner.invoke(get_application_from_module)
        assert result.exit_code == 1

    def test_get_application_from_module_missing_type(self):
        runner = CliRunner()
        result = runner.invoke(get_application_from_module)
        assert result.exit_code == 1

    def test_perform_search_applications_missing_name(self):
        runner = CliRunner()
        result = runner.invoke(perform_search_applications)
        assert result.exit_code == 1
