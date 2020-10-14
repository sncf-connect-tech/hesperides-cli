from click.testing import CliRunner

from hesperidescli.applications.platforms.properties import get_properties

from .test_utils import (
    init_client_config,
    mock_server,
    setup_function,
    teardown_function,
)


PROPERTIES_API_TEST_OUTPUT = """
{
    "key_value_properties": [
        { "name": "FOO", "value": "BAR" }
    ],
    "iterable_properties": [],
    "properties_version_id": 0
}
"""


def test_properties_export():
    init_client_config()
    with mock_server(content=PROPERTIES_API_TEST_OUTPUT):
        result = CliRunner(mix_stderr=False).invoke(
            get_properties, args=" --app APP --ptf PTF --path PATH --export"
        )
        assert result.exit_code == 0, result.output or result.exception
        assert result.output == 'export FOO="BAR"\n'
