from typer.testing import CliRunner

from cowsayrandom.main import app

runner = CliRunner()


def test_hello_world():
    result = runner.invoke(app, "hello-world")
    assert result.exit_code == 0
    assert "Hello world" in result.stdout
