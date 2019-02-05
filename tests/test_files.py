from click.testing import CliRunner
import unittest

from hesperidescli.files import get_files


class TestFiles(unittest.TestCase):
    def test_get_files_missing_args(self):
        result = CliRunner().invoke(get_files)
        assert result.exit_code == 2
        result = CliRunner().invoke(get_files, ["--application-name", "toto"])
        assert result.exit_code == 2
        result = CliRunner().invoke(
            get_files, ["--application-name", "toto", "--platform-name", "titi"]
        )
        assert result.exit_code == 2
        result = CliRunner().invoke(
            get_files,
            ["--application-name", "toto", "--platform-name", "titi", "--path", "#"],
        )
        assert result.exit_code == 2
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
        assert result.exit_code == 2
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
        assert result.exit_code == 2
