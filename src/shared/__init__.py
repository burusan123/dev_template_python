"""
共有モジュール。

アプリケーションの異なる部分で共有される機能を提供します。
"""

from .errors import (
    AuthenticationError,
    AuthorizationError,
    BaseApplicationError,
    BusinessLogicError,
    ConfigurationError,
    ExternalServiceError,
    ValidationError,
)
from .security import (
    is_safe_filename,
    mask_email,
    mask_sensitive_data,
    sanitize_log_message,
    validate_input_length,
)

__all__ = [
    # エラークラス
    "AuthenticationError",
    "AuthorizationError",
    "BaseApplicationError",
    "BusinessLogicError",
    "ConfigurationError",
    "ExternalServiceError",
    "ValidationError",
    # セキュリティ関数
    "is_safe_filename",
    "mask_email",
    "mask_sensitive_data",
    "sanitize_log_message",
    "validate_input_length",
]
