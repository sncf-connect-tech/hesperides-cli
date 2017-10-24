from click.testing import CliRunner
import unittest

from hesperidescli.cache.cache import delete_application_cache, delete_release_module_cache, \
    delete_release_template_package_cache, delete_workingcopy_module_cache, delete_workingcopy_template_package_cache, \
    regenerate_application_cache, regenerate_module_cache, regenerate_template_package_cache


class TestCache(unittest.TestCase):
    def test_delete_application_cache_missing_application_name(self):
        runner = CliRunner()
        result = runner.invoke(delete_application_cache)
        assert result.exit_code == 1
        assert result.output == '--application_name required\nAborted!\n'

    def test_delete_application_cache_missing_platform_name(self):
        runner = CliRunner()
        result = runner.invoke(delete_application_cache, ['--application_name', 'toto'])
        assert result.exit_code == 1
        assert result.output == '--platform_name required\nAborted!\n'

    def test_delete_release_module_cache_missing_module_name(self):
        runner = CliRunner()
        result = runner.invoke(delete_release_module_cache)
        assert result.exit_code == 1
        assert result.output == '--module_name required\nAborted!\n'

    def test_delete_release_module_cache_missing_module_version(self):
        runner = CliRunner()
        result = runner.invoke(delete_release_module_cache, ['--module_name', 'toto'])
        assert result.exit_code == 1
        assert result.output == '--module_version required\nAborted!\n'

    def test_delete_release_template_package_cache_missing_template_name(self):
        runner = CliRunner()
        result = runner.invoke(delete_release_template_package_cache)
        assert result.exit_code == 1
        assert result.output == '--template_name required\nAborted!\n'

    def test_delete_release_template_package_cache_missing_template_version(self):
        runner = CliRunner()
        result = runner.invoke(delete_release_template_package_cache, ['--template_name', 'toto'])
        assert result.exit_code == 1
        assert result.output == '--template_version required\nAborted!\n'

    def test_delete_workingcopy_module_cache_missing_module_name(self):
        runner = CliRunner()
        result = runner.invoke(delete_workingcopy_module_cache)
        assert result.exit_code == 1
        assert result.output == '--module_name required\nAborted!\n'

    def test_delete_workingcopy_module_cache_missing_module_version(self):
        runner = CliRunner()
        result = runner.invoke(delete_workingcopy_module_cache, ['--module_name', 'toto'])
        assert result.exit_code == 1
        assert result.output == '--module_version required\nAborted!\n'

    def test_delete_workingcopy_template_package_cache_missing_template_name(self):
        runner = CliRunner()
        result = runner.invoke(delete_workingcopy_template_package_cache)
        assert result.exit_code == 1
        assert result.output == '--template_name required\nAborted!\n'

    def test_delete_workingcopy_template_package_cache_missing_template_version(self):
        runner = CliRunner()
        result = runner.invoke(delete_workingcopy_template_package_cache, ['--template_name', 'toto'])
        assert result.exit_code == 1
        assert result.output == '--template_version required\nAborted!\n'

    def test_regenerate_application_cache_missing_template_version(self):
        runner = CliRunner()
        result = runner.invoke(regenerate_application_cache)
        assert result.exit_code == 1
        assert result.output == '--application_name required\nAborted!\n'

    def test_regenerate_application_cache_missing_platform_name(self):
        runner = CliRunner()
        result = runner.invoke(regenerate_application_cache, ['--application_name', 'toto'])
        assert result.exit_code == 1
        assert result.output == '--platform_name required\nAborted!\n'

    def test_regenerate_module_cache_missing_module_name(self):
        runner = CliRunner()
        result = runner.invoke(regenerate_module_cache)
        assert result.exit_code == 1
        assert result.output == '--module_name required\nAborted!\n'

    def test_regenerate_module_cache_missing_module_version(self):
        runner = CliRunner()
        result = runner.invoke(regenerate_module_cache, ['--module_name', 'toto'])
        assert result.exit_code == 1
        assert result.output == '--module_version required\nAborted!\n'

    def test_regenerate_template_package_cache_missing_template_name(self):
        runner = CliRunner()
        result = runner.invoke(regenerate_template_package_cache)
        assert result.exit_code == 1
        assert result.output == '--template_name required\nAborted!\n'

    def test_regenerate_template_package_cache_missing_template_version(self):
        runner = CliRunner()
        result = runner.invoke(regenerate_template_package_cache, ['--template_name', 'toto'])
        assert result.exit_code == 1
        assert result.output == '--template_version required\nAborted!\n'
