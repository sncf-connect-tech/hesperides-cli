from click.testing import CliRunner
import unittest

from hesperidescli.technos import (
    create_techno,
    create_techno_workingcopy,
    delete_techno_release,
    delete_techno_workingcopy,
    get_techno_release,
    get_techno_release_model,
    get_techno_workingcopy,
    get_techno_workingcopy_model,
    get_technos_release,
    get_technos_workingcopy,
    perform_search_technos,
    update_techno_workingcopy,
)


class TestTechnos(unittest.TestCase):
    def test_create_techno_missing_args(self):
        result = CliRunner().invoke(create_techno, ["--from-version", "1.0.0"])
        assert result.exit_code == 2
        result = CliRunner().invoke(create_techno, ["--from-name", "toto"])
        assert result.exit_code == 2
        result = CliRunner().invoke(create_techno)
        assert result.exit_code == 2

    def test_create_techno_workingcopy_missing_args(self):
        result = CliRunner().invoke(create_techno_workingcopy)
        assert result.exit_code == 2
        result = CliRunner().invoke(create_techno_workingcopy, ["--name", "toto"])
        assert result.exit_code == 2
        result = CliRunner().invoke(
            create_techno_workingcopy, ["--name", "toto", "--version", "1.0.0"],
        )
        assert result.exit_code == 2
        result = CliRunner().invoke(
            create_techno_workingcopy,
            ["--name", "toto", "--version", "1.0.0", "--template-name", "titi",],
        )
        assert result.exit_code == 2

    def test_delete_techno_release_missing_args(self):
        result = CliRunner().invoke(delete_techno_release)
        assert result.exit_code == 2
        result = CliRunner().invoke(delete_techno_release, ["--name", "toto"])
        assert result.exit_code == 2

    def test_delete_techno_workingcopy_missing_args(self):
        result = CliRunner().invoke(delete_techno_workingcopy)
        assert result.exit_code == 2
        result = CliRunner().invoke(delete_techno_workingcopy, ["--name", "toto"])
        assert result.exit_code == 2

    def test_get_techno_release_missing_args(self):
        result = CliRunner().invoke(get_techno_release)
        assert result.exit_code == 2
        result = CliRunner().invoke(get_techno_release, ["--name", "toto"])
        assert result.exit_code == 2
        result = CliRunner().invoke(
            get_techno_release, ["--name", "toto", "--version", "1.0.0"]
        )
        assert result.exit_code == 2

    def test_get_techno_release_model_missing_args(self):
        result = CliRunner().invoke(get_techno_release_model)
        assert result.exit_code == 2
        result = CliRunner().invoke(get_techno_release_model, ["--name", "toto"])
        assert result.exit_code == 2

    def test_get_techno_workingcopy_missing_args(self):
        result = CliRunner().invoke(get_techno_workingcopy)
        assert result.exit_code == 2
        result = CliRunner().invoke(get_techno_workingcopy, ["--name", "toto"])
        assert result.exit_code == 2
        result = CliRunner().invoke(
            get_techno_workingcopy, ["--name", "toto", "--version", "1.0.0"],
        )
        assert result.exit_code == 2

    def test_get_techno_workingcopy_model_missing_args(self):
        result = CliRunner().invoke(get_techno_workingcopy_model)
        assert result.exit_code == 2
        result = CliRunner().invoke(get_techno_workingcopy_model, ["--name", "toto"])
        assert result.exit_code == 2

    def test_get_technos_release_missing_args(self):
        result = CliRunner().invoke(get_technos_release)
        assert result.exit_code == 2
        result = CliRunner().invoke(get_technos_release, ["--name", "toto"])
        assert result.exit_code == 2

    def test_get_technos_workingcopy_missing_args(self):
        result = CliRunner().invoke(get_technos_workingcopy)
        assert result.exit_code == 2
        result = CliRunner().invoke(get_technos_workingcopy, ["--name", "toto"])
        assert result.exit_code == 2

    def test_perform_search_technos_missing_terms(self):
        result = CliRunner().invoke(perform_search_technos)
        assert result.exit_code == 2

    def test_update_techno_workingcopy_missing_args(self):
        result = CliRunner().invoke(update_techno_workingcopy)
        assert result.exit_code == 2
        result = CliRunner().invoke(update_techno_workingcopy, ["--name", "toto"])
        assert result.exit_code == 2
        result = CliRunner().invoke(
            update_techno_workingcopy, ["--name", "toto", "--version", "1.0.0"],
        )
        assert result.exit_code == 2
        result = CliRunner().invoke(
            update_techno_workingcopy,
            ["--name", "toto", "--version", "1.0.0", "--template-name", "titi",],
        )
        assert result.exit_code == 2
