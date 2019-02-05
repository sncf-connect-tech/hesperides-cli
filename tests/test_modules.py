from click.testing import CliRunner

from hesperidescli.modules import get_modules

from .test_utils import (
    init_client_config,
    mock_server,
    setup_function,
    teardown_function,
)


def test_get_modules():
    init_client_config()
    with mock_server(content="[]"):
        result = CliRunner(mix_stderr=False).invoke(get_modules)
        assert result.exit_code == 0, result.output or result.exception
