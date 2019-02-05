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
        assert result.exit_code == 2
        assert (
            result.output
            == """Usage: get-application [OPTIONS] APPLICATION_NAME
Try "get-application --help" for help.

Error: Missing argument "APPLICATION_NAME".
"""
        )

    def test_get_applications_using_module_missing_args(self):
        result = CliRunner().invoke(get_applications_using_module)
        assert result.exit_code == 2
        result = CliRunner().invoke(get_applications_using_module, ["--module", "toto"])
        assert result.exit_code == 2
        result = CliRunner().invoke(
            get_applications_using_module, ["--module", "toto", "--version", "titi"]
        )
        assert result.exit_code == 2

    def test_perform_search_applications_missing_name(self):
        result = CliRunner().invoke(perform_search_applications)
        assert result.exit_code == 2
