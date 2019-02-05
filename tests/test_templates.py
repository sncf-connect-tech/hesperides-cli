from click.testing import CliRunner
import unittest

from hesperidescli.templates import (
    create_template_package,
    create_template_package_workingcopy,
    delete_template_package_release,
    delete_template_package_workingcopy,
    get_template_package_release,
    get_template_package_release_model,
    get_template_package_workingcopy,
    get_template_package_workingcopy_model,
    get_templates_packages_release,
    get_templates_packages_workingcopy,
    perform_search_templates_packages,
    update_template_package_workingcopy,
)


class TestTemplates(unittest.TestCase):
    def test_create_template_package_missing_args(self):
        result = CliRunner().invoke(
            create_template_package, ["--from-package-version", "1.0.0"]
        )
        assert result.exit_code == 2
        result = CliRunner().invoke(
            create_template_package, ["--from-package-name", "toto"]
        )
        assert result.exit_code == 2
        result = CliRunner().invoke(create_template_package)
        assert result.exit_code == 2

    def test_create_template_package_workingcopy_missing_args(self):
        result = CliRunner().invoke(create_template_package_workingcopy)
        assert result.exit_code == 2
        result = CliRunner().invoke(
            create_template_package_workingcopy, ["--package-name", "toto"]
        )
        assert result.exit_code == 2
        result = CliRunner().invoke(
            create_template_package_workingcopy,
            ["--package-name", "toto", "--package-version", "1.0.0"],
        )
        assert result.exit_code == 2
        result = CliRunner().invoke(
            create_template_package_workingcopy,
            [
                "--package-name",
                "toto",
                "--package-version",
                "1.0.0",
                "--template-name",
                "titi",
            ],
        )
        assert result.exit_code == 2

    def test_delete_template_package_release_missing_args(self):
        result = CliRunner().invoke(delete_template_package_release)
        assert result.exit_code == 2
        result = CliRunner().invoke(
            delete_template_package_release, ["--package-name", "toto"]
        )
        assert result.exit_code == 2

    def test_delete_template_package_workingcopy_missing_args(self):
        result = CliRunner().invoke(delete_template_package_workingcopy)
        assert result.exit_code == 2
        result = CliRunner().invoke(
            delete_template_package_workingcopy, ["--package-name", "toto"]
        )
        assert result.exit_code == 2

    def test_get_template_package_release_missing_args(self):
        result = CliRunner().invoke(get_template_package_release)
        assert result.exit_code == 2
        result = CliRunner().invoke(
            get_template_package_release, ["--package-name", "toto"]
        )
        assert result.exit_code == 2
        result = CliRunner().invoke(
            get_template_package_release,
            ["--package-name", "toto", "--package-version", "1.0.0"],
        )
        assert result.exit_code == 2

    def test_get_template_package_release_model_missing_args(self):
        result = CliRunner().invoke(get_template_package_release_model)
        assert result.exit_code == 2
        result = CliRunner().invoke(
            get_template_package_release_model, ["--package-name", "toto"]
        )
        assert result.exit_code == 2

    def test_get_template_package_workingcopy_missing_args(self):
        result = CliRunner().invoke(get_template_package_workingcopy)
        assert result.exit_code == 2
        result = CliRunner().invoke(
            get_template_package_workingcopy, ["--package-name", "toto"]
        )
        assert result.exit_code == 2
        result = CliRunner().invoke(
            get_template_package_workingcopy,
            ["--package-name", "toto", "--package-version", "1.0.0"],
        )
        assert result.exit_code == 2

    def test_get_template_package_workingcopy_model_missing_args(self):
        result = CliRunner().invoke(get_template_package_workingcopy_model)
        assert result.exit_code == 2
        result = CliRunner().invoke(
            get_template_package_workingcopy_model, ["--package-name", "toto"]
        )
        assert result.exit_code == 2

    def test_get_templates_packages_release_missing_args(self):
        result = CliRunner().invoke(get_templates_packages_release)
        assert result.exit_code == 2
        result = CliRunner().invoke(
            get_templates_packages_release, ["--package-name", "toto"]
        )
        assert result.exit_code == 2

    def test_get_templates_packages_workingcopy_missing_args(self):
        result = CliRunner().invoke(get_templates_packages_workingcopy)
        assert result.exit_code == 2
        result = CliRunner().invoke(
            get_templates_packages_workingcopy, ["--package-name", "toto"]
        )
        assert result.exit_code == 2

    def test_perform_search_templates_packages_missing_terms(self):
        result = CliRunner().invoke(perform_search_templates_packages)
        assert result.exit_code == 2

    def test_update_template_package_workingcopy_missing_args(self):
        result = CliRunner().invoke(update_template_package_workingcopy)
        assert result.exit_code == 2
        result = CliRunner().invoke(
            update_template_package_workingcopy, ["--package-name", "toto"]
        )
        assert result.exit_code == 2
        result = CliRunner().invoke(
            update_template_package_workingcopy,
            ["--package-name", "toto", "--package-version", "1.0.0"],
        )
        assert result.exit_code == 2
        result = CliRunner().invoke(
            update_template_package_workingcopy,
            [
                "--package-name",
                "toto",
                "--package-version",
                "1.0.0",
                "--template-name",
                "titi",
            ],
        )
        assert result.exit_code == 2
