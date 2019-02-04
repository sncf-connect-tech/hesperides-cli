from click.testing import CliRunner
import unittest

from hesperidescli.files import get_files


class TestFiles(unittest.TestCase):
    def test_get_files_missing_application_name(self):
        result = CliRunner().invoke(get_files)
        assert result.output == "--application-name required\nAborted!\n"

    def test_get_files_missing_platform_name(self):
        result = CliRunner().invoke(get_files, ["--application-name", "toto"])
        assert result.output == "--platform-name required\nAborted!\n"

    def test_get_files_missing_path(self):
        result = CliRunner().invoke(
            get_files, ["--application-name", "toto", "--platform-name", "titi"]
        )
        assert result.output == "--path required\nAborted!\n"

    def test_get_files_missing_module_name(self):
        result = CliRunner().invoke(
            get_files,
            ["--application-name", "toto", "--platform-name", "titi", "--path", "#"],
        )
        assert result.output == "--module-name required\nAborted!\n"

    def test_get_files_missing_module_version(self):
        result = CliRunner().invoke(
            get_files,
            [
                "--application-name",
                "toto",
                "--platform-name",
                "titi",
                "--path",
                "#",
                "--module-name",
                "tata",
            ],
        )
        assert result.output == "--module-version required\nAborted!\n"

    def test_get_files_missing_instance_name(self):
        result = CliRunner().invoke(
            get_files,
            [
                "--application-name",
                "toto",
                "--platform-name",
                "titi",
                "--path",
                "#",
                "--module-name",
                "tata",
                "--module-version",
                "1.0.0",
            ],
        )
        assert result.output == "--instance-name required\nAborted!\n"
