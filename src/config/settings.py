from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    アプリケーションの設定を管理するクラス。

    .envファイルや環境変数から設定値を読み込みます。
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    APP_NAME: str = "dev-template-python"
    LOG_LEVEL: str = "INFO"


settings = Settings()
