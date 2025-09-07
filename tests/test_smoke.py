import importlib


def test_import_core() -> None:
    module = importlib.import_module("core")
    assert module is not None


def test_cli_main_help() -> None:
    """CLIのヘルプが正常に表示されることを確認する。"""
    from typer.testing import CliRunner

    from core.cli import app

    runner = CliRunner()
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "dev-template-python" in result.stdout
