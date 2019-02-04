from hesperidescli.local import generate, validate

import pytest


def test_generate_and_validate():
    with pytest.raises(SystemExit) as exit:
        generate.main(["tests/descriptor.json"])
    assert exit.value.code == 0

    assert open("tests/app-props.yml").read() == "root:\n  key: value-bar"
    assert open("tests/app.properties").read() == "[root]\nconfig: value"
    assert open("tests/app2.properties").read() == "[root]\nconfig: value"

    with pytest.raises(SystemExit) as exit:
        validate.main(["tests/descriptor.json"])
    assert exit.value.code == 0
