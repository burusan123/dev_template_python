# Python Project Template

## 概要

これは、**VibeCoding**という開発プロセスに最適化された、堅牢で保守性の高いPythonアプリケーションを迅速に開発するための標準テンプレートです。
`src`レイアウト、静的コード解析、テスト、CI/CD連携、自動コードフォーマット、そして**AIエージェントとの協調開発**の仕組みが予め組み込まれています。

## 主な特徴

- **モダンなパッケージ管理**: `pyproject.toml` (PEP 621) を採用し、`setuptools`でビルドします。
- **高品質なコード**:
  - [**Ruff**](https://github.com/astral-sh/ruff): 高速なリンターとフォーマッター。
  - [**Mypy**](http://mypy-lang.org/): 静的型チェッカー。
- **堅牢なテスト**:
  - [**pytest**](https://pytest.org/): 実践的なテストフレームワーク。
- **自動化された品質チェック**:
  - [**pre-commit**](https://pre-commit.com/): コミット前に自動でフォーマットとLintチェックを実行。
- **包括的なセキュリティ対策**:
  - [**detect-secrets**](https://github.com/Yelp/detect-secrets): 秘密情報の検出と防止。
  - [**bandit**](https://github.com/PyCQA/bandit): Pythonコードのセキュリティ脆弱性検出。
  - [**safety**](https://github.com/pyupio/safety): 依存関係の脆弱性チェック。
  - [**CodeQL**](https://codeql.github.com/): GitHubによる高度な静的解析エンジン。
  - **セキュリティユーティリティ**: ログマスキング、入力検証、安全なファイル名チェック。
- **設定管理**:
  - [**pydantic-settings**](https://docs.pydantic.dev/latest/concepts/pydantic_settings/): 型安全な設定管理。
  - **環境変数**: `.env`ファイルからの自動読み込み。
- **CLI機能**:
  - [**Typer**](https://typer.tiangolo.com/): モダンなCLIアプリケーション。
  - **設定表示**: `dev-template show-config`で現在の設定を確認。
- **AI協調開発**:
  - **AGENTS.md**: AIエージェント向けの詳細な操作マニュアル。
  - **実装計画テンプレート**: AIが自律的に実装できる包括的な計画書。
- **CI/CD連携**:
  - **GitHub Actions**: Pull Request時に自動でテスト、コード解析、セキュリティチェックを実行。

## 新しいプロジェクトの始め方

1.  **テンプレートリポジトリのクローン**:
    -   まず、このテンプレートリポジトリを、新しいプロジェクト名でクローンします。
    ```bash
    git clone https://github.com/burusan123/dev_template_python.git your-new-project-name
    cd your-new-project-name
    ```

2.  **Git履歴の初期化**:
    -   テンプレートのGit履歴を削除し、新しいプロジェクトとしてまっさらな状態から始めます。
    ```bash
    rm -rf .git
    git init -b main
    ```

3.  **プロジェクト情報の更新**:
    - `pyproject.toml`を開き、`name`, `version`, `description`, `authors`などを新しいプロジェクトに合わせて修正します。

4.  **ローカル環境のセットアップ**:
    -   Pythonの高速なパッケージ管理ツール`uv`をインストールし、仮想環境の作成、ライブラリのインストール、pre-commitフックの有効化を行います。
    ```bash
    # uvのインストール (未インストールの場合)
    pip install uv

    # 仮想環境を作成
    uv venv

    # 仮想環境を有効化 (Windows: .venv\Scripts\activate | macOS/Linux: source .venv/bin/activate)

    # ロックファイルから依存関係と開発ツールをインストール
    uv pip sync requirements.lock
    python -m pre_commit install

    # 環境設定ファイルの作成
    cp .env.example .env
    # .envファイルを編集して、必要な設定値を入力
    ```

5.  **リモートリポジトリの設定**:
    -   GitHubなどで新しい空のリポジトリを作成してください。
    -   作成したリポジトリのURLを、このローカルリポジトリのリモートとして設定します。
    ```bash
    git remote add origin https://github.com/your-org/your-new-project-name.git
    ```

6.  **最初のコミットとプッシュ**:
    -   すべての変更をコミットし、リモートリポジトリにプッシュします。
    ```bash
    git add .
    git commit -m "Initial commit from template"
    git push -u origin main
    ```

## ディレクトリ構成

```
.
├── .cursor/rules/      # Cursor AI アシスタント用のルール定義
├── .github/workflows/  # GitHub Actions のワークフロー定義
├── .vscode/            # VS Code / Cursor のエディタ設定
├── data/               # プロジェクトで使用するデータ（Git管理外）
├── docs/               # ドキュメント
│   ├── development/    # 開発関連ドキュメント
│   └── SECURITY.md     # セキュリティガイドライン
├── scripts/            # ちょっとしたスクリプト
├── src/                # Pythonのソースコード
│   ├── config/         # 設定管理
│   ├── core/           # アプリケーションの中核ロジック
│   ├── domain/         # ドメイン固有のロジック
│   ├── pipelines/      # データ処理などのパイプライン
│   ├── shared/         # 複数箇所で共有されるモジュール
│   └── utils/          # 汎用的なユーティリティ
└── tests/              # テストコード
├── AGENTS.md           # AIエージェント向け操作マニュアル
├── .env.example        # 環境変数テンプレート
├── .pre-commit-config.yaml # pre-commitフックの設定
├── .secrets.baseline   # detect-secrets ベースライン
└── pyproject.toml      # プロジェクト定義と依存関係
```

### 各ディレクトリの役割

`src`配下の各ディレクトリは、関心の分離(Separation of Concerns)の原則に基づき、それぞれが明確に異なる責任を持っています。依存関係は常に一方向（`utils` ← `shared` ← `core`）に保たれ、逆方向の依存は許可されません。

> **Note: サンプルコードについて**
>
> このテンプレートには、アーキテクチャの理解を助けるために「商品(Item)」というドメインのサンプルコードが含まれています。
>
> *   `src/domain/models/item.py`
> *   `src/core/services/item_service.py`
> *   `tests/core/services/test_item_service.py`
>
> 実際のプロジェクトを開始する際には、**これらのサンプルファイルは削除してください**。そして、あなた自身のドメインモデルとサービスを、これらのファイルの構造を参考にして作成してください。

| ディレクトリ | 役割                                       | 依存の方向 (`→` は「に依存する」)      | 主な中身の例                                           |
| :----------- | :----------------------------------------- | :----------------------------------- | :------------------------------------------------------------------- |
| `src/config` | **設定管理層**<br>アプリケーション全体の設定を一元管理。 | (なし)                               | 環境変数、設定値の型安全な管理 |
| `src/utils`  | **汎用ツール層**<br>プロジェクトに全く依存しない、独立した関数群。 | (なし)                               | 日付・文字列操作、純粋なアルゴリズムなど |
| `src/shared` | **共通インフラ層**<br>プロジェクト全体で共有する技術的な機能。 | `shared` → `utils`, `config`         | ロギング設定、セキュリティ機能、カスタム例外など |
| `src/core`   | **アプリケーション層**<br>ビジネスプロセスを組み立てるワークフロー。 | `core` → `shared`, `domain`, `config` | 複数のドメインオブジェクトを操作するユースケース、CLI機能など |
| `src/domain` | **ドメイン層**<br>アプリケーションの心臓部となる純粋なビジネスルール。 | `domain` → `utils` (稀に)            | `User`や`Product`といったビジネスエンティティなど |

この構造により、変更が他の部分に影響を与えにくい、柔軟でスケールしやすいアプリケーションが実現できます。

## 開発ワークフロー

### VibeCodingによる開発プロセス

私たちのチームでは、LLM（大規模言語モデル）を活用した「VibeCoding」という開発プロセスを採用しています。
このプロセスは、LLMとの対話コンテキストを意図的に短く保ち、各ステップの成果物をドキュメントとして明確に残すことで、AIとの共同作業における安定性と一貫性を高めることを目的としています。

#### VibeCodingの核心思想

VibeCodingは単なる「AIにお願いする」コーディングスタイルではありません。これは、**人間の設計意図を最大限に尊重し、AIの能力を安全かつ効率的に引き出すためのソフトウェア工学的手法**です。このテンプレートは、以下の思想に基づいています。

1.  **実装計画書は「マスタープロンプト」である**:
    *   実装フェーズでは、`implementation_plan.md`が**唯一絶対の仕様書（マスタープロンプト）**となります。
    *   AIエージェントは、この計画書に書かれたタスク、完了条件、テスト要件に**忠実に**従います。計画書にない機能の追加や自己判断による仕様変更は行いません。
    *   これにより、人間の設計意図からの逸脱を防ぎ、開発の再現性を担保します。

2.  **AIの役割はフェーズで変化する**:
    *   **設計フェーズ**: AIは**経験豊富なシニアアーキテクト**として、多様な選択肢やリスクを提示し、創造性を発揮します。
    *   **実装フェーズ**: AIは**忠実なジュニア開発者**として、計画書に基づき、正確で質の高いコードを生成することに集中します。

3.  **自動化された品質ゲートは「安全なサンドボックス」である**:
    *   本テンプレートに組み込まれたLint、型チェック、テストカバレッジ、アーキテクチャ依存関係チェック、セキュリティスキャンは、単なる品質ツールではありません。
    *   これらは、AIが自律的にコードを生成・変更しても**越えてはならない境界を技術的に強制する**ための「安全なサンドボックス」として機能します。
    *   このサンドボックスがあるからこそ、人間はマイクロマネジメントから解放され、高レベルな指示とレビューに集中できます。

この思想を理解し、`AGENTS.md`のルールを遵守することが、本テンプレートを最大限に活用する鍵となります。

> **重要: AIエージェント向けマニュアル**
> 
> AIエージェント（Cursor AI、ChatGPT、Claude等）と協調開発を行う際は、必ず [`AGENTS.md`](./AGENTS.md) を参照してください。
> このファイルには、AIが遵守すべき操作仕様、制約、受入条件が詳細に定義されています。

> **Note**
> LLMとの対話で得られた知見や問題解決の記録は、[`docs/development/llm_knowhow.md`](./docs/development/llm_knowhow.md) に蓄積しています。
> 開発を始める前に一度目を通し、新しい知見が得られた場合は積極的に追記してください。
> 記入例は [`docs/development/llm_knowhow.sample.md`](./docs/development/llm_knowhow.sample.md) を参照してください。

#### 基本ステップ

1.  **設計フェーズ (1〜4)**:
    -   `1. 全体設計` → `2. 詳細設計` の順で、LLMと対話しながら設計ドキュメントを作成します。各ステップの区切りでコンテキストをクリアすることを推奨します。

2.  **計画フェーズ (5)**:
    -   `5. 実装計画`: 詳細設計に基づき、[`implementation_plan_template.md`](./docs/development/implementation_plan_template.md) をコピーして、実装計画書を作成します。この計画書は、実装フェーズにおける**マスタープロンプト**となります。AIが自律的にタスクを遂行できるよう、全体方針、タスクの完了条件、テスト要件などを可能な限り詳細に記述します。

3.  **実装フェーズ (6〜)**:
    -   `6. (コンテキストクリア)`: **実装を開始する前に、必ずLLMとの会話をリセットします。**
    -   `7. 実装`: 作成した実装計画書**全体**をLLMに読み込ませ、「*計画書に従い、Task 1から実装を開始してください*」といった高レベルな指示を与えます。
    -   `8. レビューと進行`: LLMが生成したコードをレビューし、問題がなければ「*Task 2に進んでください*」のように次のタスクを指示します。このサイクルを計画書のタスクがすべて完了するまで繰り返します。
    -   `9. ログ記録`: タスクが完了するたびに、[`docs/development/dev_log.md`](./docs/development/dev_log.md)に進捗を記録します。(記入例は [`docs/development/dev_log.sample.md`](./docs/development/dev_log.sample.md) を参照)

### コミット規約

本プロジェクトでは、コミット履歴を分かりやすく保ち、リリース作業を自動化するために **Conventional Commits** の規約を採用しています。
コミットメッセージは、以下の形式で記述してください。

```
<type>[optional scope]: <description>
```

**主な`<type>`:**

-   `feat`: 新しい機能を追加した場合
-   `fix`: バグを修正した場合
-   `docs`: ドキュメントのみを更新した場合
-   `style`: コードの動作に影響しない、フォーマットなどの変更
-   `refactor`: リファクタリング（バグ修正や機能追加ではないコード変更）
-   `test`: テストの追加や修正
-   `chore`: ビルドプロセスや補助ツールの変更など

### リリース手順

このリポジトリでは `release-please` を利用して、リリースプロセスが自動化されています。

1.  **Pull Requestのマージ**: `feat:` や `fix:` などの接頭辞が付いたコミットを含むPull Requestが `main` ブランチにマージされると、GitHub Actionsが起動します。
2.  **リリースPRの自動作成**: `release-please`がコミット履歴を分析し、次のバージョン番号を判断して、`CHANGELOG.md`を自動更新するPull Requestを作成します。
3.  **リリースの実行**: 自動作成されたリリースPRをマージすると、GitHub上で新しいバージョンがリリースされ、対応するタグが作成されます。

---

- **依存関係の追加**:
  新しいライブラリを追加する場合は、まず`pyproject.toml`の`[project.dependencies]`セクションに追記します。
  その後、以下のコマンドを実行して`requirements.lock`ファイルを更新します。
  ```bash
  uv pip compile pyproject.toml --all-extras -o requirements.lock
  ```

- **コードの静的解析とフォーマット**:
  - `git commit`を実行すると、`pre-commit`が自動でコードをチェック・修正します。
  - 手動で実行する場合は以下のコマンドを使用します。
    ```bash
    # Lintチェック
    ruff check .
    # フォーマット
    ruff format .
    # 型チェック
    mypy .
    ```

- **テストの実行**:
  ```bash
  pytest
  ```

- **セキュリティチェック**:
  ```bash
  # 秘密情報の検出
  detect-secrets scan --force-use-all-plugins .
  
  # セキュリティ脆弱性の検出
  bandit -r src/
  
  # 依存関係の脆弱性チェック
  safety check
  ```

- **CLI機能の使用**:
  ```bash
  # 現在の設定を表示
  dev-template show-config
  
  # サンプル商品を作成（サンプルコード）
  dev-template create-item --id 1 --name "Sample Product" --price 100.0
  
  # ヘルプを表示
  dev-template --help
  ```

## CI/CD

このリポジトリでは、`main`ブランチへのPull Requestが作成されると、`.github/workflows/ci.yml`に定義されたGitHub Actionsが自動的に実行されます。
CIパイプラインでは、以下のチェックが実行され、コードの品質とセキュリティを保証します：

- **コード品質**: Ruff（lint + format）、Mypy（型チェック）
- **テスト**: pytest による全テスト実行
- **セキュリティ**: detect-secrets、bandit による脆弱性検出
- **高度なセキュリティスキャン**: CodeQL による詳細なコード解析

## セキュリティ

このテンプレートは、セキュリティファーストの開発を支援します：

- **自動セキュリティチェック**: コミット時とCI/CDでの自動検証
- **セキュリティユーティリティ**: ログマスキング、入力検証、安全なファイル名チェック
- **包括的なガイドライン**: [`docs/SECURITY.md`](./docs/SECURITY.md) に詳細な指針を記載

詳細は [`docs/SECURITY.md`](./docs/SECURITY.md) を参照してください。

## 設定管理

アプリケーションの設定は `src/config/settings.py` で一元管理されています：

```python
from config import settings

# 設定値の取得
app_name = settings.APP_NAME
log_level = settings.LOG_LEVEL
```

環境変数は `.env` ファイルから自動的に読み込まれます。`.env.example` をコピーして使用してください。

<!-- chore: trigger CI -->
