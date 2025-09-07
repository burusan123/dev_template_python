"""
shared.errorsモジュールのテスト。
"""

from shared.errors import (
    AuthenticationError,
    AuthorizationError,
    BaseApplicationError,
    BusinessLogicError,
    ConfigurationError,
    ExternalServiceError,
    ValidationError,
)


class TestBaseApplicationError:
    """BaseApplicationError例外のテスト。"""

    def test_create_with_message_only(self) -> None:
        """メッセージのみで例外を作成できることをテストします。"""
        error = BaseApplicationError("Test error")
        assert str(error) == "Test error"
        assert error.message == "Test error"
        assert error.error_code is None

    def test_create_with_message_and_code(self) -> None:
        """メッセージとエラーコードで例外を作成できることをテストします。"""
        error = BaseApplicationError("Test error", "TEST_001")
        assert str(error) == "Test error"
        assert error.message == "Test error"
        assert error.error_code == "TEST_001"


class TestValidationError:
    """ValidationError例外のテスト。"""

    def test_default_message(self) -> None:
        """デフォルトメッセージが設定されることをテストします。"""
        error = ValidationError()
        assert error.message == "入力データが無効です"
        assert error.error_code == "VALIDATION_ERROR"

    def test_custom_message(self) -> None:
        """カスタムメッセージが設定されることをテストします。"""
        error = ValidationError("カスタムエラー")
        assert error.message == "カスタムエラー"
        assert error.error_code == "VALIDATION_ERROR"


class TestAuthenticationError:
    """AuthenticationError例外のテスト。"""

    def test_default_message(self) -> None:
        """デフォルトメッセージが設定されることをテストします。"""
        error = AuthenticationError()
        assert error.message == "認証が必要です"
        assert error.error_code == "AUTHENTICATION_ERROR"

    def test_custom_message(self) -> None:
        """カスタムメッセージが設定されることをテストします。"""
        error = AuthenticationError("ログインしてください")
        assert error.message == "ログインしてください"
        assert error.error_code == "AUTHENTICATION_ERROR"


class TestAuthorizationError:
    """AuthorizationError例外のテスト。"""

    def test_default_message(self) -> None:
        """デフォルトメッセージが設定されることをテストします。"""
        error = AuthorizationError()
        assert error.message == "この操作を実行する権限がありません"
        assert error.error_code == "AUTHORIZATION_ERROR"

    def test_custom_message(self) -> None:
        """カスタムメッセージが設定されることをテストします。"""
        error = AuthorizationError("管理者権限が必要です")
        assert error.message == "管理者権限が必要です"
        assert error.error_code == "AUTHORIZATION_ERROR"


class TestConfigurationError:
    """ConfigurationError例外のテスト。"""

    def test_default_message(self) -> None:
        """デフォルトメッセージが設定されることをテストします。"""
        error = ConfigurationError()
        assert error.message == "設定に問題があります"
        assert error.error_code == "CONFIGURATION_ERROR"

    def test_custom_message(self) -> None:
        """カスタムメッセージが設定されることをテストします。"""
        error = ConfigurationError("データベース設定が無効です")
        assert error.message == "データベース設定が無効です"
        assert error.error_code == "CONFIGURATION_ERROR"


class TestExternalServiceError:
    """ExternalServiceError例外のテスト。"""

    def test_default_message(self) -> None:
        """デフォルトメッセージが設定されることをテストします。"""
        error = ExternalServiceError()
        assert error.message == "外部サービスとの通信に失敗しました"
        assert error.error_code == "EXTERNAL_SERVICE_ERROR"

    def test_custom_message(self) -> None:
        """カスタムメッセージが設定されることをテストします。"""
        error = ExternalServiceError("API呼び出しがタイムアウトしました")
        assert error.message == "API呼び出しがタイムアウトしました"
        assert error.error_code == "EXTERNAL_SERVICE_ERROR"


class TestBusinessLogicError:
    """BusinessLogicError例外のテスト。"""

    def test_requires_message(self) -> None:
        """メッセージが必須であることをテストします。"""
        error = BusinessLogicError("在庫が不足しています")
        assert error.message == "在庫が不足しています"
        assert error.error_code == "BUSINESS_LOGIC_ERROR"


class TestExceptionInheritance:
    """例外の継承関係のテスト。"""

    def test_all_errors_inherit_from_base(self) -> None:
        """すべてのカスタム例外がBaseApplicationErrorを継承していることをテストします。"""
        errors = [
            ValidationError(),
            AuthenticationError(),
            AuthorizationError(),
            ConfigurationError(),
            ExternalServiceError(),
            BusinessLogicError("test"),
        ]

        for error in errors:
            assert isinstance(error, BaseApplicationError)
            assert isinstance(error, Exception)
