from __future__ import annotations

import typer
from config import settings
from rich.console import Console

from core.services import item_service
from shared.logging import get_logger, setup_logging

# typerアプリケーションを作成
app = typer.Typer(
    name="dev-template-python",
    help="堅牢で保守性の高いPythonアプリケーションを迅速に開発するための標準テンプレートです。",
    add_completion=False,
)
console = Console()


@app.callback()
def callback() -> None:
    """アプリケーションのセットアップ(ロギングなど)を行います。"""
    setup_logging()


@app.command()
def show_config() -> None:
    """現在のアプリケーション設定を表示します。"""
    logger = get_logger(__name__)
    logger.info("現在の設定:")
    # settingsオブジェクトを辞書に変換して表示
    console.print(settings.model_dump())


@app.command()
def create_item(
    item_id: int = typer.Option(1, "--id", help="商品ID"),
    name: str = typer.Option("Sample Item", "--name", help="商品名"),
    price: float = typer.Option(100.0, "--price", help="価格"),
) -> None:
    """新しい商品を作成し、その情報を表示します。"""
    logger = get_logger(__name__)
    logger.info(f"商品を作成します: id={item_id}, name='{name}', price={price}")

    try:
        item = item_service.create_item(item_id=item_id, name=name, price=price)
        logger.info("商品が正常に作成されました。")
        console.print(item.model_dump())
    except ValueError as e:
        logger.error(f"商品の作成に失敗しました: {e}")
        raise typer.Exit(code=1) from e


def main() -> None:
    """CLIアプリケーションのエントリーポイント。"""
    app()


if __name__ == "__main__":
    main()
