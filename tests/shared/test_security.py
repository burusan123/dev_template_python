"""
shared.securityモジュールのテスト。
"""

import pytest

from shared.security import (
    is_safe_filename,
    mask_email,
    mask_sensitive_data,
    sanitize_log_message,
    validate_input_length,
)


class TestMaskEmail:
    """mask_email関数のテスト。"""

    def test_mask_normal_email(self) -> None:
        """通常のメールアドレスが正しくマスクされることをテストします。"""
        result = mask_email("user@example.com")
        assert result == "u***@example.com"

    def test_mask_short_email(self) -> None:
        """短いメールアドレスが正しくマスクされることをテストします。"""
        result = mask_email("a@b.co")
        assert result == "a***@b.co"

    def test_mask_single_char_local(self) -> None:
        """ローカル部が1文字のメールアドレスが正しくマスクされることをテストします。"""
        result = mask_email("x@example.com")
        assert result == "x***@example.com"

    def test_mask_invalid_email(self) -> None:
        """無効なメールアドレスが正しく処理されることをテストします。"""
        result = mask_email("invalid-email")
        assert result == "***"

    def test_mask_empty_email(self) -> None:
        """空文字列が正しく処理されることをテストします。"""
        result = mask_email("")
        assert result == "***"


class TestMaskSensitiveData:
    """mask_sensitive_data関数のテスト。"""

    def test_mask_email_field(self) -> None:
        """emailフィールドが正しくマスクされることをテストします。"""
        data = {"email": "user@example.com", "name": "John"}
        result = mask_sensitive_data(data)
        assert result == {"email": "u***@example.com", "name": "John"}

    def test_mask_password_field(self) -> None:
        """passwordフィールドが正しくマスクされることをテストします。"""
        data = {"password": "secret123", "username": "john"}
        result = mask_sensitive_data(data)
        assert result == {"password": "***", "username": "john"}

    def test_mask_multiple_sensitive_fields(self) -> None:
        """複数の機密フィールドが正しくマスクされることをテストします。"""
        data = {
            "email": "user@example.com",
            "password": "secret",
            "api_key": "sk-1234567890",
            "name": "John"
        }
        result = mask_sensitive_data(data)
        expected = {
            "email": "u***@example.com",
            "password": "***",
            "api_key": "***",
            "name": "John"
        }
        assert result == expected

    def test_no_sensitive_data(self) -> None:
        """機密データがない場合、元のデータが返されることをテストします。"""
        data = {"name": "John", "age": 30}
        result = mask_sensitive_data(data)
        assert result == data


class TestSanitizeLogMessage:
    """sanitize_log_message関数のテスト。"""

    def test_sanitize_email_in_message(self) -> None:
        """メッセージ内のメールアドレスがマスクされることをテストします。"""
        message = "User user@example.com logged in"
        result = sanitize_log_message(message)
        assert result == "User u***@example.com logged in"

    def test_sanitize_api_key_in_message(self) -> None:
        """メッセージ内のAPIキーがマスクされることをテストします。"""
        message = "API key sk-1234567890abcdef used"
        result = sanitize_log_message(message)
        assert result == "API key *** used"

    def test_sanitize_uuid_in_message(self) -> None:
        """メッセージ内のUUIDがマスクされることをテストします。"""
        message = "Processing request 123e4567-e89b-12d3-a456-426614174000"
        result = sanitize_log_message(message)
        assert result == "Processing request ***"

    def test_sanitize_clean_message(self) -> None:
        """機密情報がないメッセージがそのまま返されることをテストします。"""
        message = "User logged in successfully"
        result = sanitize_log_message(message)
        assert result == message


class TestValidateInputLength:
    """validate_input_length関数のテスト。"""

    def test_validate_normal_input(self) -> None:
        """通常の入力が正しく処理されることをテストします。"""
        result = validate_input_length("hello", 10)
        assert result == "hello"

    def test_validate_max_length_input(self) -> None:
        """最大長の入力が正しく処理されることをテストします。"""
        result = validate_input_length("hello", 5)
        assert result == "hello"

    def test_truncate_long_input(self) -> None:
        """長すぎる入力が切り詰められることをテストします。"""
        result = validate_input_length("hello world", 5)
        assert result == "hello"

    def test_validate_empty_input_raises_error(self) -> None:
        """空の入力でValueErrorが発生することをテストします。"""
        with pytest.raises(ValueError, match="入力値が空です"):
            validate_input_length("")


class TestIsSafeFilename:
    """is_safe_filename関数のテスト。"""

    def test_safe_filename(self) -> None:
        """安全なファイル名がTrueを返すことをテストします。"""
        assert is_safe_filename("document.txt") is True
        assert is_safe_filename("my_file.pdf") is True
        assert is_safe_filename("data-2023.csv") is True

    def test_unsafe_filename_with_path_traversal(self) -> None:
        """パストラバーサルを含むファイル名がFalseを返すことをテストします。"""
        assert is_safe_filename("../secret.txt") is False
        assert is_safe_filename("folder/../file.txt") is False

    def test_unsafe_filename_with_dangerous_chars(self) -> None:
        """危険な文字を含むファイル名がFalseを返すことをテストします。"""
        assert is_safe_filename("file<script>.txt") is False
        assert is_safe_filename("file|pipe.txt") is False
        assert is_safe_filename('file"quote.txt') is False

    def test_unsafe_reserved_names(self) -> None:
        """予約されたファイル名がFalseを返すことをテストします。"""
        assert is_safe_filename("CON") is False
        assert is_safe_filename("PRN") is False
        assert is_safe_filename("COM1") is False

    def test_empty_filename(self) -> None:
        """空のファイル名がFalseを返すことをテストします。"""
        assert is_safe_filename("") is False
