from click.testing import CliRunner
import unittest

from hesperidescli.files.files import get_files


class TestFiles(unittest.TestCase):
    def test_get_files_missing_application_name(self):
        runner = CliRunner()
        result = runner.invoke(get_files)
        assert result.output == '--application_name required\nAborted!\n'

    def test_get_files_missing_platform_name(self):
        runner = CliRunner()
        result = runner.invoke(get_files, ['--application_name', 'toto'])
        assert result.output == '--platform_name required\nAborted!\n'

    def test_get_files_missing_path(self):
        runner = CliRunner()
        result = runner.invoke(get_files, ['--application_name', 'toto', '--platform_name', 'titi'])
        assert result.output == '--path required\nAborted!\n'

    def test_get_files_missing_module_name(self):
        runner = CliRunner()
        result = runner.invoke(get_files, ['--application_name', 'toto', '--platform_name', 'titi', '--path', '#'])
        assert result.output == '--module_name required\nAborted!\n'

    def test_get_files_missing_module_version(self):
        runner = CliRunner()
        result = runner.invoke(get_files,
                               ['--application_name', 'toto', '--platform_name', 'titi', '--path', '#', '--module_name',
                                'tata'])
        assert result.output == '--module_version required\nAborted!\n'

    def test_get_files_missing_instance_name(self):
        runner = CliRunner()
        result = runner.invoke(get_files,
                               ['--application_name', 'toto', '--platform_name', 'titi', '--path', '#', '--module_name',
                                'tata', '--module_version', '1.0.0'])
        assert result.output == '--instance_name required\nAborted!\n'