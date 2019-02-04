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
    def test_create_template_package_missing_from_package_name_when_from_package_version_is_given(
        self
    ):
        result = CliRunner().invoke(
            create_template_package, ["--from-package-version", "1.0.0"]
        )
        assert (
            result.output
            == "--from-package-name required when --from-package-version is given\nAborted!\n"
        )

    def test_create_template_package_missing_from_package_version_when_from_package_name_is_given(
        self
    ):
        result = CliRunner().invoke(
            create_template_package, ["--from-package-name", "toto"]
        )
        assert (
            result.output
            == "--from-package-version required when --from-package-name is given\nAborted!\n"
        )

    def test_create_template_package_missing_body(self):
        result = CliRunner().invoke(create_template_package)
        assert result.output == "--body required\nAborted!\n"

    def test_create_template_package_workingcopy_missing_package_name(self):
        result = CliRunner().invoke(create_template_package_workingcopy)
        assert result.output == "--package-name required\nAborted!\n"

    def test_create_template_package_workingcopy_missing_package_version(self):
        result = CliRunner().invoke(
            create_template_package_workingcopy, ["--package-name", "toto"]
        )
        assert result.output == "--package-version required\nAborted!\n"

    def test_create_template_package_workingcopy_missing_template_name(self):
        result = CliRunner().invoke(
            create_template_package_workingcopy,
            ["--package-name", "toto", "--package-version", "1.0.0"],
        )
        assert result.output == "--template-name required\nAborted!\n"

    def test_create_template_package_workingcopy_missing_body(self):
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
        assert result.output == "--body required\nAborted!\n"

    def test_delete_template_package_release_missing_package_name(self):
        result = CliRunner().invoke(delete_template_package_release)
        assert result.output == "--package-name required\nAborted!\n"

    def test_delete_template_package_release_missing_package_version(self):
        result = CliRunner().invoke(
            delete_template_package_release, ["--package-name", "toto"]
        )
        assert result.output == "--package-version required\nAborted!\n"

    def test_delete_template_package_workingcopy_missing_package_name(self):
        result = CliRunner().invoke(delete_template_package_workingcopy)
        assert result.output == "--package-name required\nAborted!\n"

    def test_delete_template_package_workingcopy_missing_package_version(self):
        result = CliRunner().invoke(
            delete_template_package_workingcopy, ["--package-name", "toto"]
        )
        assert result.output == "--package-version required\nAborted!\n"

    def test_get_template_package_release_missing_package_name(self):
        result = CliRunner().invoke(get_template_package_release)
        assert result.output == "--package-name required\nAborted!\n"

    def test_get_template_package_release_missing_package_version(self):
        result = CliRunner().invoke(
            get_template_package_release, ["--package-name", "toto"]
        )
        assert result.output == "--package-version required\nAborted!\n"

    def test_get_template_package_release_missing_template_name(self):
        result = CliRunner().invoke(
            get_template_package_release,
            ["--package-name", "toto", "--package-version", "1.0.0"],
        )
        assert result.output == "--template-name required\nAborted!\n"

    def test_get_template_package_release_model_missing_package_name(self):
        result = CliRunner().invoke(get_template_package_release_model)
        assert result.output == "--package-name required\nAborted!\n"

    def test_get_template_package_release_model_missing_package_version(self):
        result = CliRunner().invoke(
            get_template_package_release_model, ["--package-name", "toto"]
        )
        assert result.output == "--package-version required\nAborted!\n"

    def test_get_template_package_workingcopy_missing_package_name(self):
        result = CliRunner().invoke(get_template_package_workingcopy)
        assert result.output == "--package-name required\nAborted!\n"

    def test_get_template_package_workingcopy_missing_package_version(self):
        result = CliRunner().invoke(
            get_template_package_workingcopy, ["--package-name", "toto"]
        )
        assert result.output == "--package-version required\nAborted!\n"

    def test_get_template_package_workingcopy_missing_template_name(self):
        result = CliRunner().invoke(
            get_template_package_workingcopy,
            ["--package-name", "toto", "--package-version", "1.0.0"],
        )
        assert result.output == "--template-name required\nAborted!\n"

    def test_get_template_package_workingcopy_model_missing_package_name(self):
        result = CliRunner().invoke(get_template_package_workingcopy_model)
        assert result.output == "--package-name required\nAborted!\n"

    def test_get_template_package_workingcopy_model_missing_package_version(self):
        result = CliRunner().invoke(
            get_template_package_workingcopy_model, ["--package-name", "toto"]
        )
        assert result.output == "--package-version required\nAborted!\n"

    def test_get_templates_packages_release_missing_package_name(self):
        result = CliRunner().invoke(get_templates_packages_release)
        assert result.output == "--package-name required\nAborted!\n"

    def test_get_templates_packages_release_missing_package_version(self):
        result = CliRunner().invoke(
            get_templates_packages_release, ["--package-name", "toto"]
        )
        assert result.output == "--package-version required\nAborted!\n"

    def test_get_templates_packages_workingcopy_missing_package_name(self):
        result = CliRunner().invoke(get_templates_packages_workingcopy)
        assert result.output == "--package-name required\nAborted!\n"

    def test_get_templates_packages_workingcopy_missing_package_version(self):
        result = CliRunner().invoke(
            get_templates_packages_workingcopy, ["--package-name", "toto"]
        )
        assert result.output == "--package-version required\nAborted!\n"

    def test_perform_search_templates_packages_missing_terms(self):
        result = CliRunner().invoke(perform_search_templates_packages)
        assert result.output == "--terms required\nAborted!\n"

    def test_update_template_package_workingcopy_missing_package_name(self):
        result = CliRunner().invoke(update_template_package_workingcopy)
        assert result.output == "--package-name required\nAborted!\n"

    def test_update_template_package_workingcopy_missing_package_version(self):
        result = CliRunner().invoke(
            update_template_package_workingcopy, ["--package-name", "toto"]
        )
        assert result.output == "--package-version required\nAborted!\n"

    def test_update_template_package_workingcopy_missing_template_name(self):
        result = CliRunner().invoke(
            update_template_package_workingcopy,
            ["--package-name", "toto", "--package-version", "1.0.0"],
        )
        assert result.output == "--template-name required\nAborted!\n"

    def test_update_template_package_workingcopy_missing_body(self):
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
        assert result.output == "--body required\nAborted!\n"
