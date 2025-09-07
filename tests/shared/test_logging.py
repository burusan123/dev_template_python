import logging

from rich.logging import RichHandler

from shared.logging import setup_logging


def test_setup_logging_configures_root_logger() -> None:
    """ロガーが正しくセットアップされ、RichHandlerが使用されることを確認する。"""
    # テスト開始前にハンドラをクリア
    logging.getLogger().handlers.clear()

    try:
        setup_logging()
        root_logger = logging.getLogger()
        assert root_logger.hasHandlers()
        assert len(root_logger.handlers) == 1
        handler = root_logger.handlers[0]
        assert isinstance(handler, RichHandler)
        assert root_logger.level == logging.INFO
    finally:
        # テスト後にハンドラをクリーンアップ
        logging.getLogger().handlers.clear()


def test_setup_logging_sets_level() -> None:
    """指定されたログレベルが正しく設定されることを確認する。"""
    # テスト開始前にハンドラをクリア
    logging.getLogger().handlers.clear()

    try:
        setup_logging()
        root_logger = logging.getLogger()
        # 設定から取得されるログレベルを確認
        from config import settings

        expected_level = getattr(logging, settings.LOG_LEVEL.upper())
        assert root_logger.level == expected_level
    finally:
        logging.getLogger().handlers.clear()
