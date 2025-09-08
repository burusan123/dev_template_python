import logging

from config import settings
from rich.logging import RichHandler


def setup_logging() -> None:
    """
    richライブラリを使用して、見やすいフォーマットのロガーをセットアップします。

    ログレベルは config.settings から取得します。
    """
    log_level = settings.LOG_LEVEL.upper()

    # ロガーが重複して追加されるのを防ぐ
    if logging.getLogger().hasHandlers():
        logging.getLogger().handlers.clear()

    logging.basicConfig(
        level=log_level,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True)],
    )
    # Uvicornなどの外部ライブラリのログもRichHandlerで処理する
    logging.getLogger("uvicorn").handlers = [RichHandler(rich_tracebacks=True)]
    logging.getLogger("uvicorn.access").handlers = [RichHandler(rich_tracebacks=True)]


def get_logger(name: str) -> logging.Logger:
    """
    指定された名前でロガーを取得します。

    Args:
        name: ロガーの名前。通常は __name__ を使用します。

    Returns:
        設定済みのLoggerインスタンス。
    """
    return logging.getLogger(name)
