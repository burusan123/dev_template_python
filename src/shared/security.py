"""
セキュリティ関連のユーティリティ関数。

このモジュールでは、ログのマスキング、入力のサニタイゼーション、
その他のセキュリティ関連の共通機能を提供します。
"""

import re
from typing import Any


def mask_email(email: str) -> str:
    """
    メールアドレスをマスクします。

    Args:
        email: マスクするメールアドレス

    Returns:
        マスクされたメールアドレス(例: "u***@example.com")

    Examples:
        >>> mask_email("user@example.com")
        'u***@example.com'
        >>> mask_email("a@b.co")
        'a***@b.co'
    """
    if not email or "@" not in email:
        return "***"

    local, domain = email.split("@", 1)
    if len(local) <= 1:
        return f"{local}***@{domain}"
    return f"{local[0]}***@{domain}"


def mask_sensitive_data(data: dict[str, Any]) -> dict[str, Any]:
    """
    辞書内の機密データをマスクします。

    Args:
        data: マスクする辞書データ

    Returns:
        機密データがマスクされた辞書

    Examples:
        >>> mask_sensitive_data({"email": "user@example.com", "name": "John"})
        {'email': 'u***@example.com', 'name': 'John'}
    """
    sensitive_keys = {
        "email",
        "mail",
        "e_mail",
        "password",
        "passwd",
        "pwd",
        "token",
        "api_key",
        "secret",
        "phone",
        "tel",
        "mobile",
        "ssn",
        "social_security_number",
        "credit_card",
        "card_number",
    }

    masked_data = {}
    for key, value in data.items():
        key_lower = key.lower()

        if key_lower in sensitive_keys:
            if "email" in key_lower or "mail" in key_lower:
                masked_data[key] = mask_email(str(value)) if value else "***"
            else:
                masked_data[key] = "***"
        else:
            masked_data[key] = value

    return masked_data


def sanitize_log_message(message: str) -> str:
    """
    ログメッセージから潜在的な機密情報を除去します。

    Args:
        message: サニタイズするログメッセージ

    Returns:
        サニタイズされたログメッセージ
    """
    # メールアドレスのパターンをマスク
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    message = re.sub(email_pattern, lambda m: mask_email(m.group()), message)

    # APIキーのようなパターンをマスク(例: sk-1234567890abcdef)
    api_key_pattern = r"\b[a-zA-Z]{2,4}-[a-zA-Z0-9]{16,}\b"
    message = re.sub(api_key_pattern, "***", message)

    # UUIDのようなパターンをマスク
    uuid_pattern = r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b"
    message = re.sub(uuid_pattern, "***", message, flags=re.IGNORECASE)

    return message


def validate_input_length(value: str, max_length: int = 1000) -> str:
    """
    入力値の長さを検証し、必要に応じて切り詰めます。

    Args:
        value: 検証する文字列
        max_length: 最大許可長

    Returns:
        検証済みの文字列

    Raises:
        ValueError: 入力が空文字列の場合
    """
    if not value:
        raise ValueError("入力値が空です")

    if len(value) > max_length:
        return value[:max_length]

    return value


def is_safe_filename(filename: str) -> bool:
    """
    ファイル名が安全かどうかを検証します。

    Args:
        filename: 検証するファイル名

    Returns:
        安全な場合True、そうでなければFalse
    """
    if not filename:
        return False

    # 危険な文字をチェック
    dangerous_chars = {"/", "\\", "..", "<", ">", ":", '"', "|", "?", "*"}
    if any(char in filename for char in dangerous_chars):
        return False

    # 予約されたファイル名をチェック(Windows)
    reserved_names = {
        "CON",
        "PRN",
        "AUX",
        "NUL",
        "COM1",
        "COM2",
        "COM3",
        "COM4",
        "COM5",
        "COM6",
        "COM7",
        "COM8",
        "COM9",
        "LPT1",
        "LPT2",
        "LPT3",
        "LPT4",
        "LPT5",
        "LPT6",
        "LPT7",
        "LPT8",
        "LPT9",
    }
    if filename.upper() in reserved_names:
        return False

    return True
