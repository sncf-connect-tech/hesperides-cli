from click.testing import CliRunner
from httmock import urlmatch, HTTMock

from hesperidescli.modules import get_modules, upsert_module_workingcopy_template

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


def test_upsert_template_update():
    init_client_config()
    with mock_server(content='{ "version_id": 2 }'):
        result = CliRunner(mix_stderr=False).invoke(
            upsert_module_workingcopy_template,
            args="--module-name test --module-version 0.0.1-SNAPSHOT data/create-module-template.json",
        )
        assert result.exit_code == 0, result.output or result.exception


def test_upsert_template_create():
    @urlmatch(method="GET")
    def get_module(url, request):
        return {"status_code": 404, "content": "[]"}

    @urlmatch(method="POST")
    def post_module(url, request):
        return {"status_code": 201, "content": "[]"}

    init_client_config()
    with HTTMock(get_module, post_module):
        result = CliRunner(mix_stderr=False).invoke(
            upsert_module_workingcopy_template,
            args="--module-name test --module-version 0.0.1-SNAPSHOT data/create-module-template.json",
        )
        assert result.exit_code == 0, result.output or result.exception


def test_upsert_template_failure():
    init_client_config()
    with mock_server(content="[]", status_code=400):
        result = CliRunner(mix_stderr=False).invoke(
            upsert_module_workingcopy_template,
            args="--module-name test --module-version 0.0.1-SNAPSHOT data/create-module-template.json",
        )
        assert result.exit_code == 1, result.output or result.exception
