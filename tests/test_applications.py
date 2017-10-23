from click.testing import CliRunner

from hesperidescli.applications.applications import get_application


def test_missing_application_name():
    runner = CliRunner()
    result = runner.invoke(get_application)
    assert result.exit_code == 1
