from click.testing import CliRunner
import unittest

from hesperidescli.templates.templates import create_template_package, create_template_package_workingcopy, \
    delete_template_package_release, delete_template_package_workingcopy, get_template_package_release, \
    get_template_package_release_model, get_template_package_workingcopy, get_template_package_workingcopy_model, \
    get_templates_packages_release, get_templates_packages_workingcopy, perform_search_templates_packages, \
    update_template_package_workingcopy


class TestTemplates(unittest.TestCase):
    def test_create_template_package_missing_from_package_name_when_from_package_version_is_given(self):
        runner = CliRunner()
        result = runner.invoke(create_template_package, ['--from_package_version', '1.0.0'])
        assert result.output == '--from_package_name required when --from_package_version is given\nAborted!\n'

    def test_create_template_package_missing_from_package_version_when_from_package_name_is_given(self):
        runner = CliRunner()
        result = runner.invoke(create_template_package, ['--from_package_name', 'toto'])
        assert result.output == '--from_package_version required when --from_package_name is given\nAborted!\n'

    def test_create_template_package_missing_body(self):
        runner = CliRunner()
        result = runner.invoke(create_template_package)
        assert result.output == '--body required\nAborted!\n'

    def test_create_template_package_workingcopy_missing_package_name(self):
        runner = CliRunner()
        result = runner.invoke(create_template_package_workingcopy)
        assert result.output == '--package_name required\nAborted!\n'

    def test_create_template_package_workingcopy_missing_package_version(self):
        runner = CliRunner()
        result = runner.invoke(create_template_package_workingcopy, ['--package_name', 'toto'])
        assert result.output == '--package_version required\nAborted!\n'

    def test_create_template_package_workingcopy_missing_template_name(self):
        runner = CliRunner()
        result = runner.invoke(create_template_package_workingcopy,
                               ['--package_name', 'toto', '--package_version', '1.0.0'])
        assert result.output == '--template_name required\nAborted!\n'

    def test_create_template_package_workingcopy_missing_body(self):
        runner = CliRunner()
        result = runner.invoke(create_template_package_workingcopy,
                               ['--package_name', 'toto', '--package_version', '1.0.0', '--template_name', 'titi'])
        assert result.output == '--body required\nAborted!\n'

    def test_delete_template_package_release_missing_package_name(self):
        runner = CliRunner()
        result = runner.invoke(delete_template_package_release)
        assert result.output == '--package_name required\nAborted!\n'

    def test_delete_template_package_release_missing_package_version(self):
        runner = CliRunner()
        result = runner.invoke(delete_template_package_release, ['--package_name', 'toto'])
        assert result.output == '--package_version required\nAborted!\n'

    def test_delete_template_package_workingcopy_missing_package_name(self):
        runner = CliRunner()
        result = runner.invoke(delete_template_package_workingcopy)
        assert result.output == '--package_name required\nAborted!\n'

    def test_delete_template_package_workingcopy_missing_package_version(self):
        runner = CliRunner()
        result = runner.invoke(delete_template_package_workingcopy, ['--package_name', 'toto'])
        assert result.output == '--package_version required\nAborted!\n'

    def test_get_template_package_release_missing_package_name(self):
        runner = CliRunner()
        result = runner.invoke(get_template_package_release)
        assert result.output == '--package_name required\nAborted!\n'

    def test_get_template_package_release_missing_package_version(self):
        runner = CliRunner()
        result = runner.invoke(get_template_package_release, ['--package_name', 'toto'])
        assert result.output == '--package_version required\nAborted!\n'

    def test_get_template_package_release_missing_template_name(self):
        runner = CliRunner()
        result = runner.invoke(get_template_package_release, ['--package_name', 'toto', '--package_version', '1.0.0'])
        assert result.output == '--template_name required\nAborted!\n'

    def test_get_template_package_release_model_missing_package_name(self):
        runner = CliRunner()
        result = runner.invoke(get_template_package_release_model)
        assert result.output == '--package_name required\nAborted!\n'

    def test_get_template_package_release_model_missing_package_version(self):
        runner = CliRunner()
        result = runner.invoke(get_template_package_release_model, ['--package_name', 'toto'])
        assert result.output == '--package_version required\nAborted!\n'

    def test_get_template_package_workingcopy_missing_package_name(self):
        runner = CliRunner()
        result = runner.invoke(get_template_package_workingcopy)
        assert result.output == '--package_name required\nAborted!\n'

    def test_get_template_package_workingcopy_missing_package_version(self):
        runner = CliRunner()
        result = runner.invoke(get_template_package_workingcopy, ['--package_name', 'toto'])
        assert result.output == '--package_version required\nAborted!\n'

    def test_get_template_package_workingcopy_missing_template_name(self):
        runner = CliRunner()
        result = runner.invoke(get_template_package_workingcopy,
                               ['--package_name', 'toto', '--package_version', '1.0.0'])
        assert result.output == '--template_name required\nAborted!\n'

    def test_get_template_package_workingcopy_model_missing_package_name(self):
        runner = CliRunner()
        result = runner.invoke(get_template_package_workingcopy_model)
        assert result.output == '--package_name required\nAborted!\n'

    def test_get_template_package_workingcopy_model_missing_package_version(self):
        runner = CliRunner()
        result = runner.invoke(get_template_package_workingcopy_model, ['--package_name', 'toto'])
        assert result.output == '--package_version required\nAborted!\n'

    def test_get_templates_packages_release_missing_package_name(self):
        runner = CliRunner()
        result = runner.invoke(get_templates_packages_release)
        assert result.output == '--package_name required\nAborted!\n'

    def test_get_templates_packages_release_missing_package_version(self):
        runner = CliRunner()
        result = runner.invoke(get_templates_packages_release, ['--package_name', 'toto'])
        assert result.output == '--package_version required\nAborted!\n'

    def test_get_templates_packages_workingcopy_missing_package_name(self):
        runner = CliRunner()
        result = runner.invoke(get_templates_packages_workingcopy)
        assert result.output == '--package_name required\nAborted!\n'

    def test_get_templates_packages_workingcopy_missing_package_version(self):
        runner = CliRunner()
        result = runner.invoke(get_templates_packages_workingcopy, ['--package_name', 'toto'])
        assert result.output == '--package_version required\nAborted!\n'

    def test_perform_search_templates_packages_missing_terms(self):
        runner = CliRunner()
        result = runner.invoke(perform_search_templates_packages)
        assert result.output == '--terms required\nAborted!\n'

    def test_update_template_package_workingcopy_missing_package_name(self):
        runner = CliRunner()
        result = runner.invoke(update_template_package_workingcopy)
        assert result.output == '--package_name required\nAborted!\n'

    def test_update_template_package_workingcopy_missing_package_version(self):
        runner = CliRunner()
        result = runner.invoke(update_template_package_workingcopy, ['--package_name', 'toto'])
        assert result.output == '--package_version required\nAborted!\n'

    def test_update_template_package_workingcopy_missing_template_name(self):
        runner = CliRunner()
        result = runner.invoke(update_template_package_workingcopy,
                               ['--package_name', 'toto', '--package_version', '1.0.0'])
        assert result.output == '--template_name required\nAborted!\n'

    def test_update_template_package_workingcopy_missing_body(self):
        runner = CliRunner()
        result = runner.invoke(update_template_package_workingcopy,
                               ['--package_name', 'toto', '--package_version', '1.0.0', '--template_name', 'titi'])
        assert result.output == '--body required\nAborted!\n'