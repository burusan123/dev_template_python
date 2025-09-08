# セキュリティガイドライン

このプロジェクトでは、セキュリティを最優先事項として扱います。
開発者とAIエージェントは、以下のセキュリティガイドラインを厳守してください。

---

## 1. 秘密情報の管理

### 1.1. 禁止事項
- **APIキー、パスワード、トークンをコードに直接記述しない**
- **`.env`ファイルをGitにコミットしない**
- **秘密情報をログに出力しない**
- **コメントやドキュメントに機密情報を記載しない**

### 1.2. 推奨事項
- **環境変数を使用**: 設定値は`config.settings`経由で取得
- **`.env.example`を活用**: 設定項目の例を提供（値は例示のみ）
- **ログのマスキング**: PII（個人識別情報）を含む可能性のある値は必ずマスク

```python
# ❌ 悪い例
API_KEY = "sk-1234567890abcdef"
logger.info(f"User email: {user_email}")

# ✅ 良い例
from config import settings
API_KEY = settings.API_KEY
logger.info(f"User email: {user_email[:3]}***@{user_email.split('@')[1]}")
```

---

## 2. 自動セキュリティチェック

### 2.1. detect-secrets
秘密情報の検出ツール。コミット前に自動実行されます。

```bash
# 手動実行
detect-secrets scan --baseline .secrets.baseline

# 新しい秘密情報が検出された場合の対応
detect-secrets audit .secrets.baseline
```

### 2.2. bandit
Pythonコードのセキュリティ脆弱性を検出します。

```bash
# 手動実行
bandit -r src/

# 設定ファイル: pyproject.toml の [tool.bandit] セクション
```

### 2.3. pre-commit統合
以下のセキュリティチェックがコミット時に自動実行されます：
- `detect-secrets`: 秘密情報の検出
- `bandit`: セキュリティ脆弱性の検出

---

## 3. 依存関係のセキュリティ

### 3.1. 脆弱性チェック
```bash
# 依存関係の脆弱性チェック
safety check

# 特定の脆弱性の確認
pip-audit
```

### 3.2. 依存関係の最小化
- **必要最小限の依存関係のみ追加**
- **定期的な依存関係の更新**
- **未使用の依存関係の削除**

---

## 4. 入力検証・サニタイゼーション

### 4.1. 外部入力の検証
```python
from pydantic import BaseModel, Field, validator

class UserInput(BaseModel):
    email: str = Field(..., regex=r'^[^@]+@[^@]+\.[^@]+$')
    age: int = Field(..., ge=0, le=150)

    @validator('email')
    def validate_email(cls, v):
        # 追加の検証ロジック
        return v.lower().strip()
```

### 4.2. SQLインジェクション対策
- **パラメータ化クエリの使用**
- **ORMの活用**
- **動的クエリの回避**

---

## 5. ログ・監査

### 5.1. セキュリティログ
```python
from shared.logging import get_logger

logger = get_logger(__name__)

# セキュリティイベントのログ
logger.warning("Failed login attempt", extra={
    "event_type": "security",
    "ip_address": request.remote_addr,
    "user_agent": request.headers.get('User-Agent')
})
```

### 5.2. 監査証跡
- **重要な操作の記録**
- **アクセスログの保持**
- **異常なアクティビティの検出**

---

## 6. エラーハンドリング

### 6.1. 情報漏洩の防止
```python
# ❌ 悪い例 - 内部情報が漏洩する可能性
try:
    result = database.query(sql)
except Exception as e:
    return {"error": str(e)}  # データベース構造が漏洩

# ✅ 良い例 - 安全なエラーメッセージ
try:
    result = database.query(sql)
except DatabaseError:
    logger.error("Database query failed", exc_info=True)
    return {"error": "Internal server error"}
```

### 6.2. カスタム例外の活用
```python
from shared.errors import ValidationError, AuthenticationError

def authenticate_user(token: str) -> User:
    if not token:
        raise AuthenticationError("Authentication required")
    # 認証ロジック
```

---

## 7. 開発環境のセキュリティ

### 7.1. 環境分離
- **本番環境と開発環境の完全分離**
- **テストデータの使用（本番データの使用禁止）**
- **開発用の認証情報の使用**

### 7.2. ローカル開発
```bash
# .env.example をコピーして設定
cp .env.example .env
# 開発用の値を設定（本番の値は使用しない）
```

---

## 8. インシデント対応

### 8.1. セキュリティインシデントの報告
1. **即座に作業を停止**
2. **影響範囲の特定**
3. **チームリーダーへの報告**
4. **証跡の保持**

### 8.2. 対応手順
1. **問題の封じ込め**
2. **根本原因の調査**
3. **修正の実装**
4. **再発防止策の策定**

---

## 9. セキュリティチェックリスト

### 9.1. 開発時
- [ ] 秘密情報をコードに含めていない
- [ ] 入力検証を実装している
- [ ] エラーメッセージが情報漏洩していない
- [ ] ログに機密情報を出力していない

### 9.2. コミット前
- [ ] `pre-commit`チェックが全てパス
- [ ] `detect-secrets`でアラートなし
- [ ] `bandit`でセキュリティ問題なし

### 9.3. デプロイ前
- [ ] 依存関係の脆弱性チェック完了
- [ ] セキュリティテスト実行済み
- [ ] 設定値の検証完了

---

このガイドラインは、プロジェクトのセキュリティを維持するための最低限の要件です。
不明点がある場合は、必ずセキュリティ担当者に相談してください。
