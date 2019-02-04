from click.testing import CliRunner
import unittest

from hesperidescli.applications import (
    get_application,
    get_applications_using_module,
    perform_search_applications,
)


class TestApplications(unittest.TestCase):
    def test_get_application_missing_application_name(self):
        result = CliRunner().invoke(get_application)
        assert result.exit_code == 1
        assert result.output == "--application-name required\nAborted!\n"

    def test_get_applications_using_module_missing_module(self):
        result = CliRunner().invoke(get_applications_using_module)
        assert result.exit_code == 1
        assert result.output == "--module required\nAborted!\n"

    def test_get_applications_using_module_missing_version(self):
        result = CliRunner().invoke(get_applications_using_module, ["--module", "toto"])
        assert result.exit_code == 1
        assert result.output == "--version required\nAborted!\n"

    def test_get_applications_using_module_missing_type(self):
        result = CliRunner().invoke(
            get_applications_using_module, ["--module", "toto", "--version", "titi"]
        )
        assert result.exit_code == 1
        assert result.output == "--type required\nAborted!\n"

    def test_perform_search_applications_missing_name(self):
        result = CliRunner().invoke(perform_search_applications)
        assert result.exit_code == 1
        assert result.output == "--name required\nAborted!\n"
