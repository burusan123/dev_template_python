from typer.testing import CliRunner

from core.cli import app

runner = CliRunner()


def test_show_config() -> None:
    """show-configコマンドが正常に終了することを確認するテスト。"""
    result = runner.invoke(app, ["show-config"])
    assert result.exit_code == 0
    assert "APP_NAME" in result.stdout
    assert "dev-template-python" in result.stdout


def test_create_item_success() -> None:
    """create-itemコマンドが成功することを確認するテスト。"""
    result = runner.invoke(
        app,
        [
            "create-item",
            "--id",
            "123",
            "--name",
            "Test Item",
            "--price",
            "99.99",
        ],
    )
    assert result.exit_code == 0
    assert "'id': 123" in result.stdout
    assert "'name': 'Test Item'" in result.stdout
    assert "'price': 99.99" in result.stdout


def test_create_item_failure() -> None:
    """create-itemコマンドが無効な価格で失敗することを確認するテスト。"""
    result = runner.invoke(
        app,
        [
            "create-item",
            "--id",
            "456",
            "--name",
            "Invalid Item",
            "--price",
            "-10.0",  # 価格がマイナスのため、ValueErrorが発生するはず
        ],
    )
    assert result.exit_code == 1
    assert "商品の作成に失敗しました" in result.stdout
