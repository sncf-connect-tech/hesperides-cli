import os
import tempfile
import unittest

from click.testing import CliRunner

from hesperidescli.files import get_files, write_files, chmod


class TestFiles(unittest.TestCase):
    def test_missing_args(self):
        for args in (
            [],
            ["--application-name", "toto"],
            ["--application-name", "toto", "--platform-name", "titi"],
            ["--application-name", "toto", "--platform-name", "titi", "--path", "#"],
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
        ):
            assert CliRunner().invoke(get_files, args).exit_code == 2

    def test_chmod(self):
        with tempfile.NamedTemporaryFile() as tmp_file:
            chmod(tmp_file.name, {"user": " ", "group": "   ", "other": " "})
            actual_mode = os.stat(tmp_file.name).st_mode & ((1 << 15) - 1)
            assert oct(actual_mode) == "0o644"
        with tempfile.NamedTemporaryFile() as tmp_file:
            chmod(tmp_file.name, {"user": "rw", "group": "r", "other": "r"})
            actual_mode = os.stat(tmp_file.name).st_mode & ((1 << 15) - 1)
            assert oct(actual_mode) == "0o644"
        with tempfile.NamedTemporaryFile() as tmp_file:
            chmod(tmp_file.name, {"user": "rwx", "group": "rx", "other": "rx"})
            actual_mode = os.stat(tmp_file.name).st_mode & ((1 << 15) - 1)
            assert oct(actual_mode) == "0o755"
