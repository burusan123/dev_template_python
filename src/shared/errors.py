"""
共通エラークラスの定義。

このモジュールでは、アプリケーション全体で使用するカスタム例外クラスを定義します。
セキュリティを考慮し、外部に漏洩してはいけない情報を含まないエラーメッセージを提供します。
"""


class BaseApplicationError(Exception):
    """アプリケーション共通の基底例外クラス。"""

    def __init__(self, message: str, error_code: str | None = None) -> None:
        """
        基底例外を初期化します。

        Args:
            message: ユーザーに表示する安全なエラーメッセージ
            error_code: 内部的なエラーコード(ログ用)
        """
        super().__init__(message)
        self.message = message
        self.error_code = error_code


class ValidationError(BaseApplicationError):
    """入力検証エラー。"""

    def __init__(self, message: str = "入力データが無効です") -> None:
        super().__init__(message, "VALIDATION_ERROR")


class AuthenticationError(BaseApplicationError):
    """認証エラー。"""

    def __init__(self, message: str = "認証が必要です") -> None:
        super().__init__(message, "AUTHENTICATION_ERROR")


class AuthorizationError(BaseApplicationError):
    """認可エラー。"""

    def __init__(self, message: str = "この操作を実行する権限がありません") -> None:
        super().__init__(message, "AUTHORIZATION_ERROR")


class ConfigurationError(BaseApplicationError):
    """設定エラー。"""

    def __init__(self, message: str = "設定に問題があります") -> None:
        super().__init__(message, "CONFIGURATION_ERROR")


class ExternalServiceError(BaseApplicationError):
    """外部サービス連携エラー。"""

    def __init__(self, message: str = "外部サービスとの通信に失敗しました") -> None:
        super().__init__(message, "EXTERNAL_SERVICE_ERROR")


class BusinessLogicError(BaseApplicationError):
    """ビジネスロジックエラー。"""

    def __init__(self, message: str) -> None:
        super().__init__(message, "BUSINESS_LOGIC_ERROR")
